from data_ import Credentials
from curl import Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class TestConstructor:


# Проверка, что работает переход к разделу «Соусы»
    def test_open_sauses_section(self, driver):
        driver.get(Url.main_site)
        driver.find_element(*Locators.SPAN_SAUSES).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SPAN_SAUSES))
        assert driver.find_element(*Locators.SPAN_CURRENT_CONSTRUCTOR).text == "Соусы"
        
# Проверка, что работает переход к разделу «Начинки»
    def test_open_stuffing_section(self, driver):
        driver.get(Url.main_site)
        driver.find_element(*Locators.SPAN_STUFFING).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SPAN_STUFFING))
        assert driver.find_element(*Locators.SPAN_CURRENT_CONSTRUCTOR).text == "Начинки"
        
    # Проверка, что работает переход к разделу «Булки»
    def test_open_buns_section(self, driver):
        driver.get(Url.main_site)
        driver.find_element(*Locators.SPAN_STUFFING).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SPAN_STUFFING))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SPAN_BUNS))
        driver.find_element(*Locators.SPAN_BUNS).click()
        WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element(Locators.SPAN_CURRENT_CONSTRUCTOR, 'Булки'))
        assert driver.find_element(*Locators.SPAN_CURRENT_CONSTRUCTOR).text == "Булки"
 
