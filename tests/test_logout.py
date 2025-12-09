from data_ import Credentials
from curl import Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestLogout:
    # Проверка возможности входа по кнопке «Выйти» в личном кабинете
    def test_logout(self, driver):
        driver.get(Url.main_site) # Заходим на главную страницу
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click() # На главной странице кнопка "Вход в аккаунт"
        driver.find_element(*Locators.INPUT_IMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click() # На https://stellarburgers.education-services.ru/login кнопка Войти
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)) # Ждем когда станет видима кнопка "Оформить заказ"
        driver.find_element(*Locators.ACCOUNT_BUTTON).click() # Нажимаем кнопку "Личный кабинет"
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON)) # Ждем когда станет видима кнопка "Выход"
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.HEADER_LOGIN)) # Проверяем перенаправление 
        assert driver.current_url == Url.login_page

