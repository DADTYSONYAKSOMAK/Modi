import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 24310207))

    API_HASH = os.environ.get("API_HASH", "6ae19e3374cedbf288bd1a4c1427f50a")
