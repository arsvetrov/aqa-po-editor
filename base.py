from logger import logger


def json_processing(r) -> dict:
    """Receives HTTP response then validate json"""
    try:
        return r.json()
    except Exception as e:
        logger.error(f"Json processing failure.\nReason: {e}")
        return {}


def get_token(r) -> str:
    """Receives HTTP response then gets 'Bearer' authorization
    header value"""
    try:
        return r.headers.get("authorization")
    except KeyError as k:
        logger.error(f"Token header failure.\nReason: {k}")


def get_users_data(r) -> tuple:
    """Receives HTTP response, Authorization "Bearer" token,
    and current user id"""

    r_json = json_processing(r)
    try:
        token = r_json.get("token")
        #user_id = str(r_json.get("user")["id"])
        user_id = str(r_json.get("id"))
    except KeyError as k:
        logger.error(f"Incorrect key received.\nReason: {k}")
    else:
        return r, token, user_id
