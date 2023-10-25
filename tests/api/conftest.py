import pytest

from src.api.client.api_support import *
from src.api.client.api_client import Auth, UserManagement
from test_data.payloads.user_credentials import UserData


@pytest.fixture(scope="function")
def registered_admin():
    """Register a new admin-user"""
    Auth.register_user(UserData.register)


@pytest.fixture(scope="function")
def logged_admin():
    """Register a new test user with admin rights, login
     then remove test user"""

    Auth.register_user(UserData.register)
    response = Auth.login_user(UserData.login)
    user_data = get_users_data(response)
    yield
    UserManagement.delete_user(token=user_data[1], u_id=user_data[2])


@pytest.fixture(scope="function")
def remove_user():
    """Login then delete test user by id"""
    yield
    response = Auth.login_user(UserData.login)
    user_data = get_users_data(response)
    UserManagement.delete_user(token=user_data[1], u_id=user_data[2])