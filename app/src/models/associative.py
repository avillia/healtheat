from app.src.extensions.sqlalchemy import db
from app.src.models.main import BaseModel


class UserIllness(BaseModel):
    __tablename__ = "users_illnesses"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"),
    )
    illness_id = db.Column(
        db.ForeignKey("illnesses.id", ondelete="CASCADE", onupdate="CASCADE"),
    )


class RecipeIllness(BaseModel):
    __tablename__ = "recipes_for_illnesses"

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(
        db.ForeignKey("recipes.id", ondelete="CASCADE", onupdate="CASCADE"),
    )
    illness_id = db.Column(
        db.ForeignKey("illnesses.id", ondelete="CASCADE", onupdate="CASCADE"),
    )


class SavedRecipes(BaseModel):
    __tablename__ = "saved_recipes_by_user"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"),
    )
    recipe_id = db.Column(
        db.ForeignKey("recipes.id", ondelete="CASCADE", onupdate="CASCADE"),
    )
