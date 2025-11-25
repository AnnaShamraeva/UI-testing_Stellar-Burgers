from data_ import Credentials
from curl import Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestGoToPersonalAccount:
    # Переход в личный кабинет. Проверка перехода по клику на «Личный кабинет».
    def test_go_to_personal_account(self, driver):
        driver.get(Url.main_site) # Заходим на главную страницу
        driver.find_element(*Locators.ACCOUNT_BUTTON).click() # На главной странице кнопка "Вход в аккаунт"
        driver.find_element(*Locators.INPUT_IMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click() 
        WebDriverWait(driver, 15).until(EC.url_contains(Url.profile_page))
        assert driver.current_url == Url.profile_page