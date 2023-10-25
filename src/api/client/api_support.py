import re
from features.logger import logger as l


def json_processing(r) -> dict:
    """Receives HTTP response then validate json"""
    try:
        return r.json()
    except Exception as e:
        l.logger.error(f"Json processing failure.\nReason: {e}")
        return {}


def validate_token(token: str) -> str | None:
    """Receives Bearer token then search it in pattern"""
    token_pattern = r"^Bearer [A-Za-z0-9_.-]+=*$"
    return re.match(token_pattern, token)


def get_token(r) -> str:
    """Receives HTTP response, gets 'Bearer' authorization
    header value then validate it"""
    try:
        token = r.headers.get("authorization")
    except KeyError as k:
        l.logger.error(f"Token header failure.\nReason: {k}")
    else:
        token = validate_token(token)
        if token is not None:
            return token
        else:
            l.logger.error(f"Invalid token: {token} received")
            raise Exception


def get_users_data(r) -> tuple:
    """Receives HTTP response, Authorization "Bearer" token,
    and current user id"""

    r_json = json_processing(r)
    try:
        token = r_json.get("token")
        user_id = str(r_json.get("user")["id"])
    except KeyError as k:
        l.logger.error(f"Incorrect key received.\nReason: {k}")
    else:
        return r, token, user_id
