from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    LOGIN_PAGE_LOCATOR = (By.CLASS_NAME, "login_logo")
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    def do_login(self, username, password):
        self.locate_element_by_selector(self.LOGIN_PAGE_LOCATOR)
        self.do_send_keys(self.USERNAME_INPUT, username)
        self.do_send_keys(self.PASSWORD_INPUT, password)
        self.do_click(self.LOGIN_BUTTON)
        