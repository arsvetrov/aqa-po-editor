import pytest
from base import *
from poe_api import Auth, UserManagement


@pytest.fixture()
def logged_admin():
    """Register a new user, login then remove test user"""

    reg_data = {
        "email": "qa.user@p2h.com",
        "password": "123456",
        "name": "Qa User"
    }

    log_data = {
        "email": reg_data.get("email"),
        "password": reg_data.get("password")
    }

    Auth.register_user(reg_data)
    r = Auth.login_user(log_data)
    user_data = get_users_data(r)
    token = user_data[1]
    u_id = user_data[2]
    yield token, u_id
    UserManagement.delete_user(u_id, token)


@pytest.fixture(scope="function")
def remove_user():
    """Login then delete test user using API"""
    log_data = {
            "email": "user12222@p2h.com",
            "password": "123456",
    }
    r = Auth.login_user(log_data)
    r_json = json_processing(r)
    u_data = get_users_data(r_json)
    token = u_data[1]
    u_id = u_data[2]
    UserManagement.delete_user(u_id, token)






