from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.NAME, "submit")
    REGISTER_BUTTON = (By.XPATH, "//a[text()='Register']")
    NEGATIVE_MESSAGE = (By.XPATH, "//b[text() = 'Enter your Email address and password correct']")
    POSITIVE_REGISTER_FLAG = (By.ID, 'login-form')
    POSITIVE_LOGIN_FLAG = (By.XPATH, "//h4[text()='{0}']")
        
    def navigate_to_register_page(self):
        self.do_click(self.REGISTER_BUTTON)
    
    def do_login(self, email, password):
        self.do_send_keys(self.EMAIL_INPUT, email)
        self.do_send_keys(self.PASSWORD_INPUT, password)
        self.do_click(self.LOGIN_BUTTON)
        