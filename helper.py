from faker import Faker

faker  = Faker() # вспомогательная функция, генерирует рандомные данные

def generate_registration_data():
    name = faker.name()
    email = faker.email()
    password = faker.password() # опционально special_chars=True, upper_case=True, lower_case=True, lengh=6, digits=True
    return name, email, password # Возвращает кортеж (email, password)

def generate_reg_data_without_password():
    name = faker.name()
    email = faker.email()
    return name, email # Возвращает кортеж 