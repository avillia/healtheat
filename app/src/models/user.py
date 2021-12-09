from flask_user import UserMixin

from app.src.extensions.sqlalchemy import db
from app.src.models.main import BaseModel


class User(BaseModel, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(256), nullable=False, server_default="")
    active = db.Column(db.Boolean(), nullable=False, server_default="0")

    role_name = db.Column(db.ForeignKey("user_roles.name"))
    role = db.relationship("Role", back_populates="users")

    illnesses = db.relationship(
        "Illness", secondary="users_illnesses", back_populates="users"
    )
    saved_recipes = db.relationship(
        "Recipe", secondary="saved_recipes_by_user", back_populates="saved_by"
    )
