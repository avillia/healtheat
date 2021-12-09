from app.src.extensions.sqlalchemy import db
from app.src.models.main import BaseModel


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
