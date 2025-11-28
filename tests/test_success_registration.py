from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from data_ import Credentials
from helper import generate_registration_data
from curl import Url
from locators import Locators
from conftest import driver

class TestSuccessRegistration:
    def test_success_registration(self, driver):
        name, email, password = generate_registration_data()
        driver.get(Url.registration_page)
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.HEADER_LOGIN))
       

# Регестрация с паролем менее шести символов
    @pytest.mark.parametrize('password', ['1', '123', '12345'])
    def test_not_success_registration_password_less_6_digits(self, driver, password):
        driver.get(Url.registration_page)
        driver.find_element(*Locators.REG_NAME).clear()
        driver.find_element(*Locators.REG_NAME).send_keys('Иван')
        driver.find_element(*Locators.REG_EMAIL).clear()
        driver.find_element(*Locators.REG_EMAIL).send_keys('Ivan1212@gmail.com')
        driver.find_element(*Locators.REG_PASSWORD).clear()
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.HEADER_WRONG_PASSWORD, "Некорректный пароль"))
        
