import os.path
import os
import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions


# This function adds the command-line option --browser
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome or firefox")
    parser.addoption("--url")


# This fixture parses the command line option
@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def url(request):
    return request.config.getoption("--url")


# This is your main setup fixture
@pytest.fixture(scope="class", autouse=True)
def setup(request, browser, url):
    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--remote-debugging-port=9222")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        extras.append(pytest_html.extras.url(item.nodeid))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_directory = os.path.dirname(item.config.option.htmlpath)
            screenshots_directory = os.path.join(report_directory, "screenshots")
            if not os.path.exists(screenshots_directory):
                os.makedirs(screenshots_directory)

            test_name = item.nodeid.split("::")[-1]
            file_name = f"{test_name}_{int(round(time.time() * 1000))}.png"
            destinationFile = os.path.join(screenshots_directory, file_name)
            driver = item.cls.driver  # Accessing driver from the test item
            driver.save_screenshot(destinationFile)
            if file_name:
                html = f'<div><img src="{os.path.join("screenshots", file_name)}" alt="screenshot" style="width:300px;height=200px" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extras.append(pytest_html.extras.html(html))
        report.extras = extras


def pytest_html_report_title(report):
    report.title = "Automation Report"
