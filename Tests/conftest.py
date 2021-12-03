import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def init_driver(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.close()
    