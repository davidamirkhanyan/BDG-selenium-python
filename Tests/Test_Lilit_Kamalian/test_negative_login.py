import time

from Pages.PowerPage import PowerPage
import pytest

# ---------------TEST CASE VARIABLES-----------------
login_page_url = "https://www.saucedemo.com/"
negative_username = "user"
negative_password = "sauce"
expected_home_page_flag = 1


@pytest.mark.usefixtures('init_driver')
class TestRegisterLoginFlow:
    def test_positive_login(self):

        obj = PowerPage(self.driver)
        obj.navigate_by_url(login_page_url)
        obj.do_login(negative_username, negative_password)
        actual_home_page_flag = obj.locate_element_by_selector(obj.HOME_PAGE_LOCATOR)
        value_dict = {}

