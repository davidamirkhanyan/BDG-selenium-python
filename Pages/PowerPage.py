from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegistrationPage
from Pages.BasePage import BasePage


class PowerPage(LoginPage, RegistrationPage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        