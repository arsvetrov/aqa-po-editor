import pytest

from src.api.client.api_client import Auth
from src.api.client.api_support import *
from test_data.payloads.user_credentials import UserData
from test_data.responses.responses import AuthResponses


@pytest.mark.positive
def test_register01(remove_user):
    """Register user with valid data"""

    response = Auth.register_user(UserData.register)
    r_json = json_processing(response)

    assert response.status_code == 200
    assert r_json == AuthResponses.success_register


@pytest.mark.negative
def test_register02(registered_admin, remove_user):
    """Try to register user with existing email"""

    response = Auth.register_user(UserData.register)
    r_json = json_processing(response)

    assert response.status_code == 422
    assert r_json.get("errors") == AuthResponses.email_exists
    assert r_json.get("token") is None


@pytest.mark.positive
def test_login01(registered_admin, remove_user):
    """Login user with valid data."""

    response = Auth.login_user(UserData.login)
    r_json = json_processing(response)
    token = r_json.get("token")
    user_id = r_json.get("user")["id"]

    assert response.status_code == 201
    assert validate_token(token) is not None
    assert isinstance(user_id, int)
    assert r_json.get("user")["email"] == UserData.login.get("email")
    assert r_json.get("user")["name"] == UserData.register.get("name")
