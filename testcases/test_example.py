import pytest
import softest
from utilities.utils import Utils
from pages.registration_page import RegistrationPage
from ddt import ddt, file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestExampleOne(softest.TestCase):
    log = Utils.custom_logger()

    def setUp(self):
        self.ut = Utils()
        self.registration_page = RegistrationPage(self.driver)

    @pytest.mark.run(order=1)
    def test_title(self):
        # Check if the title of the page is correct
        self.log.info("Verify the title")
        assert "Welcome" in self.driver.title
        self.log.info("Title verification complete")

    @pytest.mark.run(order=2)
    @file_data("../testdata/testdata.json")
    def test_fill_and_submit_form(self, name, phone, email, country, city, username, password):
        # Step 1: Fill the registration form
        self.log.info("Start filling the form.")
        self.log.debug("Entering the name...")
        self.registration_page.enter_name(name)
        self.log.debug("Entering the phone number...")
        self.registration_page.enter_phone(phone)
        self.log.debug("Entering the email...")
        self.registration_page.enter_email(email)
        self.log.debug("Selecting the country...")
        self.registration_page.select_country(country)
        self.log.debug("Entering the city...")
        self.registration_page.enter_city(city)
        self.log.debug("Entering the Username...")
        self.registration_page.enter_username(username)
        self.log.debug("Entering the Password...")
        self.registration_page.enter_password(password)
        self.log.info("Finished filling the form")
