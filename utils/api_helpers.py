import requests
import allure
from requests_toolbelt.multipart.encoder import MultipartEncoder

from utils.urls import REGISTER_URL, LOGIN_URL, CREATE_AD_URL, UPDATE_AD_URL, DELETE_AD_URL


@allure.step("Регистрация нового пользователя")
def register_user(user_data: dict):
    return requests.post(REGISTER_URL, json=user_data)


@allure.step("Вход пользователя в систему")
def login_user(user_data: dict):
    payload = {"email": user_data["email"], "password": user_data["password"]}
    return requests.post(LOGIN_URL, json=payload)


@allure.step("Получение токена авторизации для пользователя")
def get_auth_token(user_data: dict):
    response = login_user(user_data)
    return response.json()["token"]["access_token"]


@allure.step("Создание нового объявления")
def create_ad(token: str, ad_data: dict):
    multipart_data = MultipartEncoder(
        fields={key: str(value) for key, value in ad_data.items()}
    )

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": multipart_data.content_type
    }

    return requests.post(CREATE_AD_URL, data=multipart_data, headers=headers)


@allure.step("Обновление существующего объявления")
def update_ad(token: str, ad_id: int, updated_data: dict):
    multipart_data = MultipartEncoder(
        fields={key: str(value) for key, value in updated_data.items()}
    )

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": multipart_data.content_type
    }

    return requests.patch(
        f"{UPDATE_AD_URL}{ad_id}",
        headers=headers,
        data=multipart_data
    )


@allure.step("Удаление объявления")
def delete_ad(token: str, ad_id: int):
    headers = {"Authorization": f"Bearer {token}"}
    return requests.delete(f"{DELETE_AD_URL}{ad_id}", headers=headers)