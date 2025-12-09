import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from curl import Url
from data_ import Credentials
from locators import Locators


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(Url.main_site)
    yield driver
    driver.quit()