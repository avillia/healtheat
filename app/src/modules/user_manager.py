from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager

from app.src.models import User as DBUserModel


def register_user_manager(app: Flask, db: SQLAlchemy) -> UserManager:
    return UserManager(app, db, DBUserModel)
