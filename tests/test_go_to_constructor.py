from data_ import Credentials
from curl import Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestGoToConstructor:
# Переход из личного кабинета в конструктор по клику на «Конструктор»
    def test_go_to_constructor_from_personal_account(self, driver):
        driver.get(Url.main_site) # Заходим на главную страницу
        driver.find_element(*Locators.ACCOUNT_BUTTON).click() # На главной странице кнопка "Вход в аккаунт"
        driver.find_element(*Locators.INPUT_IMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click() 
        WebDriverWait(driver, 15).until(EC.url_contains(Url.profile_page))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert driver.find_element(*Locators.DO_BURGER).is_displayed()
        
# Переход из личного кабинета в конструктор по клику на логотип Stellar Burgers.
    def test_go_to_constructor_from_logo(self, driver):
        driver.get(Url.main_site) # Заходим на главную страницу
        driver.find_element(*Locators.ACCOUNT_BUTTON).click() # На главной странице кнопка "Вход в аккаунт"
        driver.find_element(*Locators.INPUT_IMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.url_contains(Url.profile_page))
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(Locators.LOGO)).click()
        assert driver.find_element(*Locators.DO_BURGER).is_displayed()
        