import os


class Config:

    BOT_TOKEN = os.environ.get("6234817090:AAEhtiYazr1rzBUNVu8UHQuQDesh7npJ1jw")

    SESSION_NAME = ":memory:"

    API_ID = int(os.environ.get("23862583"))

    API_HASH = os.environ.get("cdb6288563a205ce92ec35bd2a7fd31e")

    CLIENT_ID = os.environ.get("755761988614-e58speba1utv9bv0tmb2j1mo9ofqfj05.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = int(os.environ.get("1994781564"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 1994781564] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
