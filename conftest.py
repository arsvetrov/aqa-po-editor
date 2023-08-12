from pprint import pprint
import pytest
from base_api import *


# @pytest.fixture()
# def logged_user():
#     data = {
#       "email": "use11r@p2h.com",
#       "password": "123456",
#     }
#
#     r1 = Auth.login_user(session, data)
#     print(r1.status_code)
#     yield