from selenium.webdriver.common.by import By

class Locators:
    # локаторы для регистрации:
    REG_BUTTON = [By.XPATH, '//button[text()="Зарегистрироваться"]'] # Кнопка "Зарегистрироваться" 
    REG_NAME = (By.XPATH, '//label[normalize-space(.)="Имя"]/following-sibling::input')
    REG_EMAIL = [By.XPATH, '//label[text()="Email"]/following-sibling::input'] #  Поле ввода почты
    REG_PASSWORD = [By.XPATH, '//label[text()="Пароль"]/following-sibling::input'] #  Поле ввода пароля
    
    # локаторы для входа:
    LOGIN_BUTTON_MAIN_PAGE = By.XPATH, '//button[text()="Войти в аккаунт"]' # На главной странице https://stellarburgers.education-services.ru/ кнопка "Вход в аккаунт"
    ACCOUNT_BUTTON = By.XPATH, '//p[text()="Личный Кабинет"]' # Кнопка "Личный кабинет"
    INPUT_IMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input' # На  https://stellarburgers.education-services.ru/login поле ввода почты
    INPUT_PASSWORD = By.XPATH, '//label[text()="Пароль"]/following-sibling::input' # На  https://stellarburgers.education-services.ru/login поле ввода пароля
    LOGIN_BUTTON_LOGIN_PAGE = By.XPATH, '//button[text()="Войти"]' # На  https://stellarburgers.education-services.ru/login кнопка Войти
    LOGIN_BUTTON_REG_PAGE = By.XPATH, '//a[text()="Войти"]' # Кнопка "Войти" на странице регистрации
    #LOGIN_BUTTON_FORGOT_PASSWORD_PAGE = (By.XPATH, "//main//div//div//p/a[normalize-space(.)='Войти']") # Кнопка "Войти" на странице восстановления пароля
    LOGIN_BUTTON_FORGOT_PASSWORD_PAGE = (By.XPATH, '//a[text()="Войти"]') # Кнопка "Войти" на странице восстановления пароля

    # Заголовки:
    HEADER_LOGIN = (By.XPATH, '//h2[text()="Вход"]') # Заголовок "Вход"
    HEADER_REGISTRATION = (By.XPATH, '//h2[text()="Регистрация"]') # Заголовок "Регистрация"
    #HEADER_WRONG_PASSWORD = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p") # Заголовок "Некорректный пароль" сообщения об ошибке
    HEADER_WRONG_PASSWORD = (By.XPATH, '//p[text()="Некорректный пароль"]') # Заголовок "Некорректный пароль" сообщения об ошибкеHEADER_USER_ALREDY_EXIST = (By.XPATH, '//h2[text()="Такой пользователь уже существует"]') # Заголовок "Такой пользователь уже существует" сообщения об ошибке
    HEADER_PROFILE = (By.XPATH, '//h2[text()="Профиль"]') # Заголовок "Профиль"
    DO_BURGER= (By.XPATH, '//h1[text()="Соберите бургер"]') # Заголовок "Соберите бургер"

    # Кнопки:
    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]') # Кнопка "Оформить заказ"
    PASSWORD_IS_FORGOT_BUTTON = [By.XPATH, '//a[text()="Восстановить пароль"]'] # Кнопка "Восстановить пароль"
    RECOVERY_BUTTON = (By.XPATH, '//button[text()="Восстановить"]') # Кнопка "Восстановить"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]') # Кнопка "Конструктор"
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]') # Кнопка "Выход"
    
    # Логотип и разделы:
    LOGO = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')
    #SPAN_BUNS = (By.XPATH, '//span[contains(@class, "text") and contains(@class, "text_type_main-default") and text()="Булки"]')
    SPAN_SAUSES = [By.XPATH, '//span[text()="Соусы"]'] # Раздел "Соусы"
    SPAN_STUFFING = [By.XPATH, '//span[text()="Начинки"]'] # Раздел "Начинки"
    SPAN_CURRENT_CONSTRUCTOR = [By.XPATH, '//div[contains(@class, "current")]/span'] # Раздел-конструктор
    SPAN_BUNS = [By.XPATH, '//h2[text()="Булки"]'] # Раздел "Булки"
    
