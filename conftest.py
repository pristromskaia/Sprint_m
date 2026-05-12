import pytest
from utils.api_helpers import register_user, get_auth_token, create_ad, delete_ad
from utils.generator import generate_user_data, generate_ad_data
from utils.responses import AUTHORISED_CODE


@pytest.fixture(scope="function")
def new_user_data():
    user_data = generate_user_data()
    register_user(user_data)
    return user_data


@pytest.fixture(scope="function")
def auth_token(new_user_data):
    return get_auth_token(new_user_data)


@pytest.fixture(scope="function")
def created_ad(auth_token):
    ad_data = generate_ad_data()
    response = create_ad(auth_token, ad_data)
    assert response.status_code == AUTHORISED_CODE
    return {
        "token": auth_token,
        "response": response,
        "ad_data": ad_data,
        "ad_id": response.json()["id"]
    }


@pytest.fixture(scope="function")
def created_ad_with_cleanup(auth_token):
    ad_data = generate_ad_data()

    response = create_ad(auth_token, ad_data)
    assert response.status_code == AUTHORISED_CODE

    ad_id = response.json()["id"]

    yield {
        "token": auth_token,
        "ad_id": ad_id,
        "ad_data": ad_data,
        "response": response
    }

    delete_ad(auth_token, ad_id)


@pytest.fixture(scope="function")
def other_user_token():
    user_data = generate_user_data()
    register_user(user_data)
    return get_auth_token(user_data)