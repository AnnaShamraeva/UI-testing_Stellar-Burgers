from data_ import Credentials
from curl import Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin:
    # Проверка возможности входа по кнопке "Войти в аккаунт" на https://stellarburgers.education-services.ru/
    def test_login_from_main_site(self, driver):
        driver.get(Url.main_site)
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*Locators.INPUT_IMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()

    # Проверка возможности входа через кнопку «Личный кабинет»
    def test_login_from_personal_account(self, driver):
        driver.get(Url.main_site)
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.INPUT_IMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()

    # Проверка возможности входа через кнопку в форме регистрации
    def test_login_from_registration_page(self, driver):
        driver.get(Url.registration_page)
        driver.find_element(*Locators.LOGIN_BUTTON_REG_PAGE).click()
        driver.find_element(*Locators.INPUT_IMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()

   
    # Проверка возможности входа через кнопку в форме восстановления пароля.
    def test_login_from_password_recovery_form(self, driver):
        driver.get(Url.main_site)
        driver.find_element(*Locators.LOGIN_BUTTON_REG_PAGE).click()
        driver.find_element(*Locators.PASSWORD_IS_FORGOT_BUTTON).click()
        driver.find_element(*Locators.RECOVERY_BUTTON).click()
        driver.find_element(*Locators.INPUT_IMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()

    # Проверка возможности входа через кнопку в форме восстановления пароля.
    def test_login_from_password_recovery_form(self, driver):
        driver.get(Url.main_site)
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*Locators.PASSWORD_IS_FORGOT_BUTTON).click()
        driver.find_element(*Locators.LOGIN_BUTTON_FORGOT_PASSWORD_PAGE).click()
        driver.find_element(*Locators.INPUT_IMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()
