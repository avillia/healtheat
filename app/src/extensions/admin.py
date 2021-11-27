from flask import Flask
from flask_admin import Admin

from app.src.views.admin import views


def register_admin(app: Flask) -> Admin:
    admin = Admin(app, "HealthEat")
    for view in views:
        admin.add_view(view)
    return admin
