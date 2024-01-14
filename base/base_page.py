import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value)))

    def wait_for_presence_of_all_elements(self, locator_type, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_all_elements_located((locator_type, locator)))

    def wait_until_element_is_clickable(self, locator_type, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable((locator_type, locator)))

    def page_scroll(self, timeout=10, interval=1):
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        start_time = time.time()
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(interval)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height or (time.time() - start_time) > timeout:
                break
            last_height = new_height
