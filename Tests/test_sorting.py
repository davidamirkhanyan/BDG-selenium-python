import time

from Pages.PowerPage import PowerPage
import pytest

# ---------------TEST CASE VARIABLES-----------------
login_page_url = "https://www.saucedemo.com/"
positive_username = "standard_user"
positive_password = "secret_sauce"



@pytest.mark.usefixtures('init_driver')
class TestSorting:
    def test_sorting(self):
        
        obj = PowerPage(self.driver)
        obj.navigate_by_url(login_page_url)
        obj.do_login(positive_username, positive_password)
        obj.sort_by('az')
        sorted_name_az = obj.get_items_names()
        obj.sort_by('za')
        sorted_name_za = obj.get_items_names()
        sorted_name_za.reverse()
        obj.sort_by('lohi')
        lohi_names = obj.get_items_names()
        lohi_prices = []
        for name in lohi_names:
            price = obj.get_item_value_by_name(name)
            lohi_prices.append(price)
        obj.sort_by('hilo')
        hilo_names = obj.get_items_names()
        hilo_prices = []
        for name in hilo_names:
            price = obj.get_item_value_by_name(name)
            hilo_prices.append(price)
        hilo_prices.reverse()
        assert sorted_name_az == sorted_name_za, "Something wrong with letter sorting."
        assert lohi_prices == hilo_prices, "Somwthing wrong with price sorting."
        


