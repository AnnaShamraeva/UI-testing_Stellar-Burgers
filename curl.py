class Url:
    main_site = 'https://stellarburgers.education-services.ru/' # адресс главной страницы
    login_page = f'{main_site}login' # адресс страницы авторизации
    registration_page = f'{main_site}register' # адресс страницы регистрации
    profile_page = f'{main_site}account/profile' # адресс страницы профиля

    api_base = f'{main_site}/api'
    auth_endpoint = f'{api_base}/signin'