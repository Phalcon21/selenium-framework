import time
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

    def test_title(self):
        assert "Welcome" in self.driver.title
        time.sleep(3)

    # @data(("Anar", "+994551234567", "anar@mail.ru", "Azerbaijan", "Baku", "AnarM", "12345"))
    # @unpack
    @file_data("../testdata/testdata.json")
    def test_fill_and_submit_form(self, name, phone, email, country, city, username, password):
        # Step 1: Fill the registration form
        self.registration_page.enter_name(name)
        self.registration_page.enter_phone(phone)
        self.registration_page.enter_email(email)
        self.registration_page.select_country(country)
        self.registration_page.enter_city(city)
        self.registration_page.enter_username(username)
        self.registration_page.enter_password(password)
        self.log.info("Finished")
        time.sleep(3)
