import requests


BASE_URL = "https://po-editor-api.demo.p2h-cd.com/api/"


class Roles:
    url = BASE_URL + "roles/"

    @staticmethod
    def get_roles(token: str) -> requests.Response:
        """Get all roles"""

        return requests.get(url=Roles.url,
                            headers={'Authorization': token})

    @staticmethod
    def post_roles(payload: dict, token: str) -> requests.Response:
        """Create user role"""

        return requests.post(url=Roles.url,
                             headers={'Authorization': token},
                             json=payload)

    @staticmethod
    def delete_roles(r_id: str, token: str) -> requests.Response:
        """Remove user role"""

        return requests.delete(url=Roles.url + r_id,
                               headers={'Authorization': token})


class Applications:
    url = BASE_URL + "applications/"

    @staticmethod
    def get_apps(token: str) -> requests.Response:
        """Get all applications"""

        return requests.get(url=Applications.url,
                            headers={'Authorization': token})

    @staticmethod
    def create_app(payload: dict, token: str) -> requests.Response:
        """Create a new application"""

        return requests.post(url=Applications.url,
                             headers={'Authorization': token},
                             json=payload)

    @staticmethod
    def find_app(app_id: int, token: str) -> requests.Response:
        """Find application by id"""

        return requests.get(url=Applications.url + str(app_id),
                            headers={'Authorization': token})

    @staticmethod
    def delete_app(app_id: int, token: str) -> requests.Response:
        """Delete application by id"""

        return requests.delete(url=Applications.url + str(app_id),
                               headers={'Authorization': token})

    @staticmethod
    def update_app(app_id: str, payload: dict, token: str) -> requests.Response:
        """Update Application"""

        return requests.patch(url=Applications.url + str(app_id),
                              headers={'Authorization': token},
                              json=payload)

    @staticmethod
    def delete_lang(app_id: int, token: str) -> requests.Response:
        """Delete language by app id"""
        # ToDo
        pass

    @staticmethod
    def update_lang(app_id: int, token: str) -> requests.Response:
        """Delete lang by app id"""
        # ToDo
        pass


class UserManagement:
    url = BASE_URL + "users/"

    @staticmethod
    def get_users(token: str) -> requests.Response:
        """Get all users"""

        return requests.get(url=UserManagement.url,
                            headers={'Authorization': token})

    @staticmethod
    def get_me(token: str) -> requests.Response:
        """Get current user"""

        return requests.get(url=UserManagement.url + "me/",
                            headers={'Authorization': token})

    @staticmethod
    def get_user(u_id: int, token: str) -> requests.Response:
        """Get user by id"""

        return requests.get(url=UserManagement.url + str(u_id),
                            headers={'Authorization': token})

    @staticmethod
    def post_user(payload: dict, token: str) -> requests.Response:
        """Create a new user"""

        return requests.post(url=UserManagement.url,
                             headers={'Authorization': token},
                             json=payload)

    @staticmethod
    def update_user(u_id: int, payload: dict, token: str) -> requests.Response:
        """Update user by id"""

        return requests.patch(url=UserManagement.url + str(u_id),
                              headers={'Authorization': token},
                              json=payload)

    @staticmethod
    def update_me(u_id: int, payload: dict, token: str) -> requests.Response:
        """Update current user"""

        return requests.patch(url=UserManagement.url + str(u_id) + "/update-me/",
                              headers={'Authorization': token},
                              json=payload)

    @staticmethod
    def delete_user(u_id: int, token: str) -> requests.Response:
        """Delete user by id"""

        return requests.delete(url=UserManagement.url + str(u_id),
                               headers={'Authorization': token})


class Auth:
    url = BASE_URL + "auth/"

    @staticmethod
    def register_user(payload: dict) -> requests.Response:
        """User registration. The system expects any email to get
        that includes '@p2h.com' domain"""

        return requests.post(url=Auth.url + "registration/",
                             json=payload)

    @staticmethod
    def login_user(payload: dict) -> requests.Response:
        """User login"""

        return requests.post(url=Auth.url + "login/",
                             json=payload)


class Translations:
    url = BASE_URL + "translations/"

    @staticmethod
    def get_translations(token: str) -> requests.Response:
        """Get all existing translations"""

        return requests.get(url=Translations.url,
                            headers={{'Authorization': token}})

    @staticmethod
    def get_translation(tr_id: str, token: str) -> requests.Response:
        """Get specific translation by id"""

        return requests.get(url=Translations.url + tr_id,
                            headers={'Authorization': token})

    @staticmethod
    def add_short_tr(payload: dict, token: str) -> requests.Response:
        """Create short translation"""

        return requests.post(url=Translations.url + "add-short/",
                             headers={'Authorization': token},
                             json=payload)

    @staticmethod
    def add_detailed_tr(payload: dict, token: str) -> requests.Response:
        """Create detailed translation"""

        return requests.post(url=Translations.url + "add-detailed/",
                             headers={'Authorization': token},
                             json=payload)

    @staticmethod
    def update_translation(tr_id: str, payload: dict, token: str) -> requests.Response:
        """Update specific translation by id"""

        return requests.patch(url=Translations.url + tr_id,
                              headers={'Authorization': token},
                              json=payload)

    @staticmethod
    def delete_translation(tr_id: str, token: str) -> requests.Response:
        """Delete specific translation by id"""

        return requests.delete(url=Translations.url + tr_id,
                               headers={'Authorization': token})


class Languages:
    url = BASE_URL + "languages/"

    @staticmethod
    def get_lang(token: str) -> requests.Response:
        """Get all languages"""

        return requests.get(url=Languages.url,
                            headers={'Authorization': token})

    @staticmethod
    def get_available_lang(token: str) -> requests.Response:
        """Get available languages"""

        return requests.get(url=Languages.url + "available/",
                            headers={'Authorization': token})

    @staticmethod
    def get_alias_lang(alias: str, token: str) -> requests.Response:
        """Get language by alias"""

        return requests.get(url=Languages.url + alias,
                            headers={'Authorization': token})

    @staticmethod
    def add_lang(payload: dict, token: str) -> requests.Response:
        """Add language to the system"""

        return requests.post(url=Languages.url + "add/",
                             headers={'Authorization': token},
                             json=payload)

    @staticmethod
    def delete_lang(alias: str, token: str) -> requests.Response:
        """Delete language by alias"""

        return requests.delete(url=Languages.url + alias,
                               headers={'Authorization': token})


class Details:
    url = BASE_URL + "details/"

    @staticmethod
    def get_details(token: str) -> requests.Response:
        """Get details"""

        return requests.get(url=Details.url,
                            headers={'Authorization': token})

    @staticmethod
    def get_detail(d_id: str, token: str) -> requests.Response:
        """Get specific detail by id"""

        return requests.get(url=Details.url + d_id,
                            headers={'Authorization': token})

    @staticmethod
    def update_detail(d_id: str, payload: dict, token: str) -> requests.Response:
        """Update specific detail by id"""

        return requests.patch(url=Details.url + d_id,
                              headers={'Authorization': token},
                              json=payload)

    @staticmethod
    def delete_detail(self, alias: str, token: str) -> requests.Response:
        """Delete specific detail by alias"""

        return self.delete(url=Details.url + alias,
                           headers={'Authorization': token})


class Pages:
    url = BASE_URL + "pages/"

    @staticmethod
    def get_all_pages(token: str) -> requests.Response:
        """Get all existing pages"""

        return requests.get(url=Pages.url,
                            headers={'Authorization': token})

    @staticmethod
    def get_page(p_id: str, token: str) -> requests.Response:
        """Get specific page by id"""

        return requests.get(url=Pages.url + p_id,
                            headers={'Authorization': token})

    @staticmethod
    def update_page(p_id: str, payload: dict, token: str) -> requests.Response:
        """Update specific page by id"""

        return requests.patch(url=Pages.url + p_id,
                              headers={'Authorization': token},
                              json=payload)

    @staticmethod
    def delete_page(p_id: str, token: str) -> requests.Response:
        """Delete specific page by id"""

        return requests.delete(url=Pages.url + p_id,
                               headers={'Authorization': token})


class TranslationValues:
    url = BASE_URL + "translation-values/"

    @staticmethod
    def get_all_translation_val(token: str) -> requests.Response:
        """Get all existing translation values"""

        return requests.get(url=TranslationValues.url,
                            headers={'Authorization': token})

    @staticmethod
    def get_translation_val(tr_id: int, token: str) -> requests.Response:
        """Get specific translation value by id"""

        return requests.get(url=TranslationValues.url + str(tr_id),
                            headers={'Authorization': token})

    @staticmethod
    def update_translation_val(self, tr_id: int, payload: dict, token: str) -> requests.Response:
        """Update translation value by id"""
        # ToDo
        pass

    @staticmethod
    def delete_translation_val(self, tr_id: int, token: str) -> requests.Response:
        """Delete translation value by id"""
        # ToDo
        pass
