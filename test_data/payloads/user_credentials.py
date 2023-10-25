class UserData:

    register = {
        "email": "qa.user@p2h.com",
        "password": "123456",
        "name": "Qa User"
    }

    login = {
        "email": register.get("email"),
        "password": register.get("password")
    }
