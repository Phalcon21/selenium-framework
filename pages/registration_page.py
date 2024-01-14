from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from base.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage(BasePage):
    # Elements
    NAME_INPUT = (By.NAME, "name")
    PHONE_INPUT = (By.NAME, "phone")
    EMAIL_INPUT = (By.NAME, "email")
    CITY_INPUT = (By.NAME, "city")
    USERNAME_INPUT = (By.XPATH, '//*[@id="load_form"]/fieldset[6]/input')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="load_form"]/fieldset[7]/input')
    COUNTRY_DROPDOWN = (By.NAME, "country")
    SUBMIT_BUTTON = (By.XPATH, "/html/body/div[3]/div/div/div/div/div/form/div[1]/div[2]/input")
    ALERT = (By.ID, "alert")

    # Methods
    def enter_name(self, name):
        name_input = self.wait_for_element(*self.NAME_INPUT)
        name_input.send_keys(name)

    def enter_phone(self, phone_number):
        phone_input = self.wait_for_element(*self.PHONE_INPUT)
        phone_input.send_keys(phone_number)

    def enter_email(self, email):
        email_input = self.wait_for_element(*self.EMAIL_INPUT)
        email_input.send_keys(email)

    def enter_city(self, city_name):
        city_input = self.wait_for_element(*self.CITY_INPUT)
        city_input.send_keys(city_name)

    def enter_username(self, username):
        username_input = self.wait_for_element(*self.USERNAME_INPUT)
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.wait_for_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

    def select_country(self, country_name):
        country_dropdown = self.wait_for_element(*self.COUNTRY_DROPDOWN)
        dropdown = Select(country_dropdown)
        dropdown.select_by_visible_text(country_name)

    def click_submit_button(self):
        submit_button = self.wait_for_element(*self.SUBMIT_BUTTON)
        print(submit_button)
        # submit_button.click()

    def success_alert_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ALERT))
        alert_message = self.wait_for_element(*self.ALERT).text
        print(alert_message)
        return alert_message
