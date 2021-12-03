from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class RegistrationPage(BasePage):
    FIRST_NAME = (By.ID, "user_firstname")
    SURNAME = (By.ID, "user_surname")
    PHONE = (By.ID, "user_phone")
    STREET = (By.ID, "user_address_attributes_street")
    CITY = (By.ID, "user_address_attributes_city")
    COUNTRY = (By.ID, "user_address_attributes_county")
    POST_CODE = (By.ID, "user_address_attributes_postcode")
    EMAIL = (By.ID, "user_user_detail_attributes_email")
    PASSWORD = (By.ID, "user_user_detail_attributes_password")
    CONFIRM_PASSWORD = (By.ID, "user_user_detail_attributes_password_confirmation")
    CREATE = (By.XPATH, "//input[@name='submit']")
    NAVIGATE_PAGE = (By.NAME, "content")


    def navigate_to_login_page(self):
        self.do_click(self.CREATE)

    def do_registration(self, first_name, surname, phone, street, city, country, post_code, email, password,
                        confirm_password):
        self.do_send_keys(self.FIRST_NAME, first_name)
        self.do_send_keys(self.SURNAME, surname)
        self.do_send_keys(self.PHONE, phone)
        self.do_send_keys(self.STREET, street)
        self.do_send_keys(self.CITY, city)
        self.do_send_keys(self.COUNTRY, country)
        self.do_send_keys(self.POST_CODE, post_code)
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PASSWORD, password)
        self.do_send_keys(self.CONFIRM_PASSWORD, confirm_password)
        self.do_click(self.CREATE)
