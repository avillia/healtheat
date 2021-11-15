from flask_user import UserMixin

from app.common.helpers.enums import Roles as RoleEnum
from app.configs.extensions import db


class BaseModel(db.Model):
    __abstract__ = True


class User(BaseModel, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64, collation='NOCASE'), unique=True)
    password = db.Column(db.String(256))
    role_name = db.Column(db.ForeignKey("user_roles.name"))

    role = db.relationship("Role", back_populates="users")
    userillnesses = db.relationship(
        "UserIllness",
        primaryjoin="UserIllness.user_id == User.id",
        back_populates="user",
    )
    saved_recipes = db.relationship(
        "SavedRecipes",
        primaryjoin="SavedRecipes,user_id == User.id",
        back_populates="user",
    )


class Role(BaseModel):
    __tablename__ = "user_roles"

    name = db.Column(db.Enum(RoleEnum), primary_key=True)
    can_manage_user_data = db.Column(db.Boolean)
    can_manage_medical_info = db.Column(db.Boolean)

    users = db.relationship("User", back_populates="role")


class Illness(BaseModel):
    __tablename__ = "illnesses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    description = db.Column(db.Text)
    advices = db.Column(db.Text)

    userillnesses = db.relationship(
        "UserIllness",
        primaryjoin="UserIllness.illness_id = Illness.id",
        back_populates="illness",
    )
    recipeillnesses = db.relationship(
        "RecipeIllness",
        primaryjoin="RecipeIllness.illness_id = Illness.id",
        back_populates="illness",
    )


class UserIllness(BaseModel):
    __tablename__ = "users_illnesses"

    user_id = db.Column(
        db.ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
    illness_id = db.Column(
        db.ForeignKey("illnesses.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )

    user = db.relationship("User", back_populates="userillnesses")
    illness = db.relationship("Illness", back_populates="userillnesses")


class Recipe(BaseModel):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.Text)

    recipeillnesses = db.relationship(
        "RecipeIllness",
        primaryjoin="RecipeIllness.illness_id = Illness.id",
        back_populates="recipe",
    )
    saved_recipes = db.relationship(
        "SavedRecipes",
        primaryjoin="SavedRecipes.illness_id = Illness.id",
        back_populates="recipe",
    )


class RecipeIllness(BaseModel):
    __tablename__ = "recipes_for_illnesses"

    recipe_id = db.Column(
        db.ForeignKey("recipes.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
    illness_id = db.Column(
        db.ForeignKey("illnesses.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )

    recipe = db.relationship("Recipe", back_populates="recipeillnesses")
    illness = db.relationship("Illness", back_populates="recipeillnesses")


class SavedRecipes(BaseModel):
    __tablename__ = "saved_recipes_by_user"

    user_id = db.Column(
        db.ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
    recipe_id = db.Column(
        db.ForeignKey("recipes.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )

    user = db.relationship("User", back_populates="saved_recipes")
    recipe = db.relationship("Recipe", back_populates="saved_recipes")
