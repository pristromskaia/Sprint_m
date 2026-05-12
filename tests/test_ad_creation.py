import allure

from utils.responses import SUCCESS_AD_CREATION_CODE


@allure.feature("Создание объявления")
class TestAdCreation:
    @allure.title("Проверка успешного создание объявления")
    def test_successful_ad_creation_returns_201(self, created_ad_with_cleanup):
        assert created_ad_with_cleanup["response"].status_code == SUCCESS_AD_CREATION_CODE
        assert "id" in created_ad_with_cleanup["response"].json()
        assert (
            created_ad_with_cleanup["response"].json()["name"]
            == created_ad_with_cleanup["ad_data"]["name"]
        )
