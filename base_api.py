import requests
from pprint import pprint
session = requests.Session()
BASE_URL = "https://po-editor-api.demo.p2h-cd.com/api/"


class Roles:

    url = BASE_URL + "roles/"

    def get_roles(self: requests.session):
        """Get all roles"""
        return self.get(Roles.url)

    def post_roles(self: requests.session, request_body: dict):
        """Create user role"""
        return self.post(Roles.url, json=request_body)

    def delete_roles(self: requests.session, r_id: str):
        """Remove user role"""
        return self.delete(Roles.url + r_id)


class Applications:
    pass


class UserManagement:

    url = BASE_URL + "users/"

    def get_users(self: requests.session):
        """Get all users"""

        return self.get(UserManagement.url)

    def get_me(self: requests.session, endpoint: str = "me/"):
        """Get current user"""
        return self.get(UserManagement.url + endpoint)

    def get_user(self: requests.session, u_id: str):
        """Get user by id"""
        return self.get(UserManagement.url + u_id)

    def post_user(self: requests.session, token, json_data: dict):
        """Create a new user"""
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        return self.post(UserManagement.url, headers=headers, json=json_data)

    def update_user(self: requests.session, json_data: dict):
        """Update user's data"""
        return self.patch(UserManagement.url, json=json_data)

    def delete_user(self: requests.session, u_id: str):
        """Delete user"""
        return self.delete(UserManagement.url + u_id)

    def update_me(self: requests.session, json_data: dict, u_id: str, endpoint: str = "update-me/"):
        """Update current user"""
        url = UserManagement.url + u_id + endpoint
        return self.patch(url, json=json_data)


class Auth:

    url = BASE_URL + "auth/"

    def login_user(self, json_data: dict):
        """User login"""
        return self.post(Auth.url + "login/", json=json_data)

    def register_user(self: requests.session, json_data: dict):
        """User registration. The system expects any email to get
        that includes '@p2h.com' domain"""
        return self.post(Auth.url + "registration/", json=json_data)


# class Translations:
#     pass
#
#
# class Languages:
#     pass
#
#
# class Details:
#     pass
#
#
# class Pages:
#     pass
#
#
# class TranslationValues:
#     pass
#

def json_processing(r):
    try:
        return r.json()
    except Exception as e:
        return {}