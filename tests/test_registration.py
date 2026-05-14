import allure

from utils.api_helpers import register_user
from utils.generator import generate_user_data
from utils.responses import DUPLICATE_EMAIL_ERROR_MESSAGE, AUTHORISED_CODE, BAD_REQUEST_CODE


@allure.feature("Регистрация нового пользователя")
class TestRegistration:

    @allure.title("Проверка успешной регистрации нового пользователя")
    def test_successful_registration_returns_201_and_access_token(self):
        response = register_user(generate_user_data())
        assert response.status_code == AUTHORISED_CODE
        assert response.json()["access_token"]
        
    @allure.title("Проверка регистрации с уже существующим email")
    def test_duplicate_registration_returns_400_and_error_message(self):
        user_data = generate_user_data()
        register_user(user_data)
        response = register_user(user_data)
        assert response.status_code == BAD_REQUEST_CODE
        assert response.json().get("message") == DUPLICATE_EMAIL_ERROR_MESSAGE
        