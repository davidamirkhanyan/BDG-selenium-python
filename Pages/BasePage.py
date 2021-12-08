from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        print("Driver initialized!!!!!!!")
        
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()
        print("Click was done!!")
        
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        print("Send keys was done!!")
        
    def get_text_from_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        text = element.text
        return text
    
    def locate_element_by_selector(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return 1
    
    def get_attr_value_from_element(self, by_locator, attr_name):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        value = element.get_attribute(attr_name)
        return value
    
    def navigate_by_url(self, url):
        self.driver.get(url)
        
    def return_element_count_on_page(self, by_locator):
        elements_list = self.driver.find_elements(*by_locator)
        count = len(elements_list)
        return count
        
        