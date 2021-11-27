from datetime import datetime

from environs import Env

env = Env()
env.read_env()

FLASK_ENV = env.str("FLASK_ENV", default="development")
PROD_ENV = FLASK_ENV == "production"

SECRET_KEY = env.str("SECRET_KEY", "don't you mind being this a secret key?")

SQLALCHEMY_DATABASE_URI = env.str("SQLALCHEMY_DATABASE_URI", "sqlite:///:memory:")
SQLALCHEMY_TRACK_MODIFICATIONS = env.bool("SQLALCHEMY_TRACK_MODIFICATIONS", False)

# Flask-User (registration and permission handling)
USER_APP_NAME = env.str("USER_APP_NAME", "HealthEat")
USER_APP_VERSION = env.str("USER_APP_VERSION", "1.0")
USER_CORPORATION_NAME = env.str("USER_CORPORATION_NAME", "avillia")
USER_COPYRIGHT_YEAR = env.int("USER_COPYRIGHT_YEAR", datetime.now().year)
USER_ENABLE_EMAIL = env.bool("USER_ENABLE_EMAIL", False)
USER_ENABLE_USERNAME = env.bool("USER_ENABLE_USERNAME", True)
USER_ENABLE_REGISTER = env.bool("USER_ENABLE_REGISTER", True)
USER_REQUIRE_RETYPE_PASSWORD = env.bool("USER_REQUIRE_RETYPE_PASSWORD", True)

# Flask-Admin configs
FLASK_ADMIN_SWATCH = env.str("FLASK_ADMIN_SWATCH", "cerulean")
