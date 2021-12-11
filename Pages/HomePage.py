import time

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class HomePage(BasePage):
    # Menu Related Selectors
    HOME_PAGE_LOCATOR = (By.CLASS_NAME, "inventory_container")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    CLOSE_BURGER_MENU = (By.ID, "react-burger-cross-btn")
    ALL_ITEMS_OPTION = (By.ID, "inventory_sidebar_link")
    ABOUT_OPTION = (By.ID, "about_sidebar_link")
    LOG_OUT_OPTION = (By.ID, "logout_sidebar_link")
    RESET_APP_STATE = (By.ID, "reset_sidebar_link")
    # Sorting Related Selectors
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    SORT_A_2_Z = (By.XPATH, "//option[@value = 'az']")
    SORT_Z_2_A = (By.XPATH, "//option[@value = 'za']")
    SORT_HIGH_2_LOW = (By.XPATH, "//option[@value = 'hilo']")
    SORT_LOW_2_HIGH = (By.XPATH, "//option[@value = 'lohi']")
    # OTHER
    SHOPING_CARD = (By.CLASS_NAME, "shopping_cart_link")
    ITEM_ADD_TO_CARD_BUTTON_BY_NAME = (By.XPATH,
    "//div[text()='{0}']/parent::a/parent::div/following-sibling::div//button")
    ITEM_VALUE_BY_NAME = (By.XPATH,
    "//div[text()='{0}']/parent::a/parent::div/following-sibling::div/div")
    ITEMS_NAMES = (By.CLASS_NAME, "inventory_item_name")
    
    def menu_navigate_to(self, navigate_to):
        self.do_click(self.BURGER_MENU)
        if navigate_to == "all_items":
            self.do_click(self.ALL_ITEMS_OPTION)
            self.do_click(self.CLOSE_BURGER_MENU)
        elif navigate_to == "about":
            self.do_click(self.ABOUT_OPTION)
        elif navigate_to == "log_out":
            self.do_click(self.LOG_OUT_OPTION)
        elif navigate_to == "reset":
            self.do_click(self.RESET_APP_STATE)
            self.do_click(self.CLOSE_BURGER_MENU)
            
    def sort_by(self, type):
        self.do_click(self.SORT_SELECT)
        if type == 'az':
            self.do_click(self.SORT_A_2_Z)
        elif type == 'za':
            self.do_click(self.SORT_Z_2_A)
        elif type == 'lohi':
            self.do_click(self.SORT_LOW_2_HIGH)
        elif type == 'hilo':
            self.do_click(self.SORT_HIGH_2_LOW)
        time.sleep(2)
            
    def navigate_to_shopping_card(self):
        self.do_click(self.SHOPING_CARD)
        
    def click_on_add_to_card_button_by_name(self, item_name):
        tuple_selector = (self.ITEM_ADD_TO_CARD_BUTTON_BY_NAME[0], self.ITEM_ADD_TO_CARD_BUTTON_BY_NAME[1].format(item_name))
        self.do_click(tuple_selector)
        
    def get_item_value_by_name(self, item_name):
        tuple_selector = (self.ITEM_VALUE_BY_NAME[0], self.ITEM_VALUE_BY_NAME[1].format(item_name))
        text = self.get_text_from_element(tuple_selector)
        return text
    
    def get_items_names(self):
        names = []
        names_elements_list = self.return_all_elements_by_tuple_selector(self.ITEMS_NAMES)
        for element in names_elements_list:
            names.append(element.text)
        return names
        

