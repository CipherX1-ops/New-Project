import os
class Config(object):
    API_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    HANDLER = os.environ.get("HANDLER", "^/")
    DB_URL = os.environ.get("DB_URL", None)
    OWNER_ID = int(os.environ.get("OWNER_ID", None))

