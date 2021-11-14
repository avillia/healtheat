from environs import Env

env = Env()
env.read_env()

FLASK_ENV = env.str("FLASK_ENV", default="development")
PROD_ENV = FLASK_ENV == "production"

SQLALCHEMY_DATABASE_URI = env.str("SQLALCHEMY_DATABASE_URI", "sqlite:///:memory:")