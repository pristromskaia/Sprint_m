import allure

from utils.api_helpers import update_ad
from utils.generator import generate_updated_ad_data
from utils.responses import SUCCESS_CODE, UNAUTHORISED_CODE


@allure.feature("Редактирование объявления")
class TestAdEditing:

    @allure.title("Проверка успешного обновления объявления")
    def test_update_ad_returns_200_and_updated_data(
        self, 
        created_ad_with_cleanup
        ):
        updated_data = generate_updated_ad_data()

        response = update_ad(
            created_ad_with_cleanup["token"],
            created_ad_with_cleanup["ad_id"],
            updated_data
        )
        assert response.status_code == SUCCESS_CODE
        assert response.json()["name"] == updated_data["name"]

    @allure.title("Проверка обновления объявления другим пользователем")
    def test_update_ad_by_other_user_returns_401(
        self, 
        created_ad_with_cleanup, 
        other_user_token
        ):
        response = update_ad(other_user_token, created_ad_with_cleanup["ad_id"], generate_updated_ad_data())
        assert response.status_code == UNAUTHORISED_CODE
