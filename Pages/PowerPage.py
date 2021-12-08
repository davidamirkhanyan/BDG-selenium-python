from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.BasePage import BasePage


class PowerPage(LoginPage, HomePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        