from test_data.payloads.user_credentials import UserData


class AuthResponses:

    success_register = {'data': {'success': True}}
    email_exists = [f"This \'email\' - \'{UserData.register['email']}\' already exists."]

