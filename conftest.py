import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from curl import Url
from data_ import Credentials
from locators import Locators


@pytest.fixture(scope='function')
def driver():
    # options = Options()
    # options.add_argument('--window-size=1920,1080') # добавили ещё настройку —-window-size запускает браузер с заданным разрешением экрана.
    # Полезно, когда нужно протестировать интерфейс в системе с определённым разрешением.
    # service = Service(r"C:\WebDriver\bin\chromedriver.exe")
    # browser = webdriver.Chrome(options=options, service=service)
    # browser.get(Url.main_site)
    driver = webdriver.Chrome()
    driver.get(Url.main_site)
    #yield browser
    #browser.quit()
    yield driver
    driver.quit()