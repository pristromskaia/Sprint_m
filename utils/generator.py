import allure
import uuid


from utils.test_data import (
    REGISTER_PASSWORD,
    SUBMIT_PASSWORD,
    AD_NAME,
    AD_CATEGORY,            
    AD_CONDITION,
    AD_CITY,
    AD_DESCRIPTION,
    AD_PRICE,
    NEW_AD_NAME,
    NEW_AD_CATEGORY,
    NEW_AD_CONDITION,
    NEW_AD_CITY,
    NEW_AD_DESCRIPTION,
    NEW_AD_PRICE,
    IMAGE_VALUE
)

@allure.step("Генерация уникального email для регистрации")
def email_generator():
    unique = uuid.uuid4().hex[:10]
    return f"test_{unique}@mail.ru"


@allure.step("Генерация данных для нового пользователя")
def generate_user_data():
    email = email_generator()
    return {
        "email": email,
        "password": REGISTER_PASSWORD,
        "submit_password": SUBMIT_PASSWORD
    }

@allure.step("Генерация данных для нового объявления")
def generate_ad_data():
    unique = uuid.uuid4().hex[:6]

    return {
        "name": f"{AD_NAME}{unique}",
        "category": AD_CATEGORY,
        "condition": AD_CONDITION,
        "city": AD_CITY,
        "description": f"{AD_DESCRIPTION}{unique}",
        "price": AD_PRICE
    }

@allure.step("Генерация данных для обновления объявления")
def generate_updated_ad_data():
    unique = uuid.uuid4().hex[:6]
    return {
        "name": f"{NEW_AD_NAME}{unique}",
        "category": NEW_AD_CATEGORY,
        "condition": NEW_AD_CONDITION,
        "city": NEW_AD_CITY,
        "description": f"{NEW_AD_DESCRIPTION} {unique}",
        "price": NEW_AD_PRICE,
        "img1": IMAGE_VALUE,
        "img2": IMAGE_VALUE,
        "img3": IMAGE_VALUE
    }