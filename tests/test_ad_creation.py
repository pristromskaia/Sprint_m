import allure

from utils.responses import SUCCESS_AD_CREATION_CODE
from utils.generator import generate_ad_data
from utils.api_helpers import create_ad, delete_ad

@allure.feature("Создание объявления")
class TestAdCreation:

    @allure.title("Проверка успешного создания объявления")
    def test_successful_ad_creation_returns_201(self, auth_token):
        ad_data = generate_ad_data()

        response = create_ad(auth_token, ad_data)
        ad_id = response.json()["id"]
        
        try:
            assert response.status_code == SUCCESS_AD_CREATION_CODE
            assert "id" in response.json()
            assert response.json()["name"] == ad_data["name"]

        finally:
            delete_ad(auth_token, ad_id)
