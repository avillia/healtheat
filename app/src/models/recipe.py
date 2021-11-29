from app.src.extensions.sqlalchemy import db
from app.src.models.illness import Illness
from app.src.models.main import BaseManager, BaseModel
from app.src.models.user import User


class RecipeManager(BaseManager):
    @property
    def verified_only(self):
        return self.filter_by(is_verified=True)

    def fetch_all_verified(self):
        return self.verified_only.all()

    def fetch_all_related_to_illness(self, illness: Illness):
        return (
            self.verified_only.join(Illness.recipes)
            .where(Illness.id == illness.id)
            .all()
        )

    def fetch_all_allowed_for_illnesses(self, illnesses: list[Illness]):
        return (
            self.verified_only.join(Illness.recipes)
            .where(Illness.name.in_(illnesses))
            .all()
        )

    def fetch_all_saved_by(self, user: User):
        return self.join(User.saved_recipes).where(User.id == user.id).all()


class Recipe(BaseModel):
    __tablename__ = "recipes"

    query_class = RecipeManager
    query: RecipeManager  # need this to resolve "unresolved attribute" warning in PyCharm

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
