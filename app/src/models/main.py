from flask_user import UserMixin

from app.src.extensions.sqlalchemy import db
from app.src.helpers.enums import Roles as RoleEnum


class BaseModel(db.Model):
    __abstract__ = True


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


class Role(BaseModel):
    __tablename__ = "user_roles"

    name = db.Column(db.Enum(RoleEnum), primary_key=True)
    can_manage_users_data = db.Column(db.Boolean)
    can_manage_medical_info = db.Column(db.Boolean)

    users = db.relationship("User", back_populates="role")


class Illness(BaseModel):
    __tablename__ = "illnesses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    users = db.relationship(
        "User", secondary="users_illnesses", back_populates="illnesses"
    )
    recipes = db.relationship(
        "Recipe", secondary="recipes_for_illnesses", back_populates="illnesses"
    )


class Recipe(BaseModel):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    is_verified = db.Column(db.String(64))
    ingredients = db.Column(db.Text)
    description = db.Column(db.Text)
    advices = db.Column(db.Text)

    illnesses = db.relationship(
        "Illness", secondary="recipes_for_illnesses", back_populates="recipes"
    )
    saved_by = db.relationship(
        "User", secondary="saved_recipes_by_user", back_populates="saved_recipes"
    )
