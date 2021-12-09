from app.src.extensions.sqlalchemy import db
from app.src.models.main import BaseModel


class Recipe(BaseModel):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    is_verified = db.Column(db.Boolean)
    preview = db.Column(db.String(256))
    ingredients = db.Column(db.Text)
    description = db.Column(db.Text)
    advices = db.Column(db.Text)

    illnesses = db.relationship(
        "Illness", secondary="recipes_for_illnesses", back_populates="recipes"
    )
    saved_by = db.relationship(
        "User", secondary="saved_recipes_by_user", back_populates="saved_recipes"
    )
