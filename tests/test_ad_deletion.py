import allure

from utils.api_helpers import delete_ad
from utils.responses import SUCCESS_DELETE_MESSAGE, SUCCESS_CODE


@allure.feature("Удаление объявления")
class TestAdDeletion:

    @allure.title("Проверка успешного удаления объявления")
    def test_successful_ad_deletion_returns_200(self, created_ad):
        response = delete_ad(
            created_ad["token"],
            created_ad["ad_id"]
        )

        assert response.status_code == SUCCESS_CODE
        assert response.json()['message'] == SUCCESS_DELETE_MESSAGE