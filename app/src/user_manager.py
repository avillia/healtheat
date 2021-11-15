from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager

from app.common.models import User


def register_user_manager(app: Flask, db: SQLAlchemy) -> UserManager:
    return UserManager(app, db, User)
