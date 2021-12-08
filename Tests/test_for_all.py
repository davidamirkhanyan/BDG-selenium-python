import time

from Pages.PowerPage import PowerPage
import pytest

# ---------------TEST CASE VARIABLES-----------------
login_page_url = "https://www.saucedemo.com/"
positive_username = "standard_user"
positive_password = "secret_sauce"
expected_home_page_flag = 1
item_name1 = "Sauce Labs Onesie"
item_name2 = "Sauce Labs Fleece Jacket"
item_name3 = "Sauce Labs Bolt T-Shirt"
item_list = [item_name1, item_name2, item_name3]
items_expected = {item_name1: "$7.99",
                  item_name2: "$49.99",
                  item_name3: "$15.99"}

@pytest.mark.usefixtures('init_driver')
class TestRegisterLoginFlow:
   def test_positive_login(self):
      
      obj = PowerPage(self.driver)
      obj.navigate_by_url(login_page_url)
      obj.do_login(positive_username, positive_password)
      actual_home_page_flag = obj.locate_element_by_selector(obj.HOME_PAGE_LOCATOR)
      value_dict = {}
      for name in item_list:
         obj.click_on_add_to_card_button_by_name(name)
         item_value = obj.get_item_value_by_name(name)
         value_dict[name] = item_value
         print(value_dict)
         time.sleep(1)
      for name in item_list:
         assert value_dict[name] == items_expected[name], f"There's something wrong with {name} item value."
      assert expected_home_page_flag == actual_home_page_flag, "When doing positive login, home page does not locates!"
       
        
        