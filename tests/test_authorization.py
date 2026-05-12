import allure

from utils.api_helpers import login_user
from utils.responses import AUTHORISED_CODE


@allure.feature("Авторизация пользователя")
class TestAuthorization:

    @allure.title("Проверка успешного входа в систему")
    def test_successful_login(self, new_user_data):
        response = login_user(new_user_data)
        assert response.status_code == AUTHORISED_CODE
        assert "token" in response.json()
        assert "access_token" in response.json()["token"]
