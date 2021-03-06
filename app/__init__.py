from flask import Flask

from app.src.extensions.admin import register_admin
from app.src.extensions.sqlalchemy import db
from app.src.extensions.user_manager import register_user_manager
from app.src.views import index_bp


def register_extensions(app: Flask):
    """
    A method to add the common extensions to the app instance

    Factories are more preferable because of them helps not to
    initially bound extensions to application

    :param app: previously initialized flask app instance
    :return: app object with extensions
    """

    register_user_manager(app, db)
    register_admin(app)

    return app


def initialize_db(app: Flask):

    db.init_app(app)
    db.create_all(app=app)

    return app


def update_blueprints(app: Flask):

    app.register_blueprint(index_bp)

    return app


def create_app(config_object="app.configs"):
    app = Flask("HealthEat", static_folder="app/src/static")
    app.config.from_object(config_object)
    initialize_db(app)
    register_extensions(app)
    update_blueprints(app)

    return app
