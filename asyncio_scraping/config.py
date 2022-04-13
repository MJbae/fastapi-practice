import json
from urllib.parse import quote_plus
from pathlib import Path
from typing import Optional


BASE_DIR = Path(__file__).resolve().parent


def get_secret(
    key: str,
    default_value: Optional[str] = None,
    json_path: str = str(BASE_DIR / "secrets.json"),
):

    with open(json_path) as f:
        secrets = json.loads(f.read())
    try:
        return secrets[key]
    except KeyError:
        if default_value:
            return default_value
        raise EnvironmentError(f"Set the {key} environment variable.")


MONGO_BASE_URL = get_secret("MONGO_BASE_URL")
MONGO_USER = get_secret("MONGO_USER")
MONGO_PASSWORD = get_secret("MONGO_PASSWORD")
MONGO_URL_DETAIL = get_secret("MONGO_URL_DETAIL")
MONGO_DB_NAME = get_secret("MONGO_DB_NAME")
NAVER_API_ID = get_secret("NAVER_API_ID")
NAVER_API_SECRET = get_secret("NAVER_API_SECRET")
MONGO_URI = MONGO_BASE_URL + \
    quote_plus(MONGO_USER) + ":" + \
    quote_plus(MONGO_PASSWORD) + MONGO_URL_DETAIL
