from app.src.extensions.sqlalchemy import db
from app.src.models.main import BaseManager, BaseModel


class IllnessManager(BaseManager):
    pass


class Illness(BaseModel):
    __tablename__ = "illnesses"

    query_class = IllnessManager
    query: IllnessManager  # need this to resolve "unresolved attribute" warning in PyCharm


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    users = db.relationship(
        "User", secondary="users_illnesses", back_populates="illnesses"
    )
    recipes = db.relationship(
        "Recipe", secondary="recipes_for_illnesses", back_populates="illnesses"
    )
