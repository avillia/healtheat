from environs import Env

env = Env()
env.read_env()

FLASK_ENV = env.str("FLASK_ENV", default="development")
PROD_ENV = FLASK_ENV == "production"

SECRET_KEY = env.str("SECRET_KEY", "don't you mind being this a secret key?")

SQLALCHEMY_DATABASE_URI = env.str("SQLALCHEMY_DATABASE_URI", "sqlite:///:memory:")
SQLALCHEMY_TRACK_MODIFICATIONS = env.bool("SQLALCHEMY_TRACK_MODIFICATIONS", False)

USER_ENABLE_EMAIL = env.bool("USER_ENABLE_EMAIL", False)
USER_ENABLE_USERNAME = env.bool("USER_ENABLE_USERNAME", False)
USER_REQUIRE_RETYPE_PASSWORD = env.bool("USER_REQUIRE_RETYPE_PASSWORD", True)
