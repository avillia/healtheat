from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager

from app.src.models import User as DBUserModel


def register_user_manager(app: Flask, db: SQLAlchemy) -> UserManager:
    """
    This workaround needed because UserManager __init__() does not
    work well with None instead of app, db and models instances, and
    its init_app() method is clunky.
    TODO: Fork Flask-User and implement correct init_app()
    """
    return UserManager(app, db, DBUserModel)
