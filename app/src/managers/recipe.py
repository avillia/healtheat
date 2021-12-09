from app.src.models import Illness, Recipe, User


class RecipeManager:
    model = Recipe

    @property
    def query_verified_only(self):
        return self.model.query.filter_by(is_verified=True)

    def fetch_all_verified(self):
        return self.query_verified_only.all()

    def fetch_all_verified_and_related_to_illness(self, illness: Illness):
        return (
            self.query_verified_only.join(Illness.recipes)
            .where(Illness.id == illness.id)
            .all()
        )

    def fetch_all_allowed_for_illnesses(self, illnesses: list[str]):
        return (
            self.query_verified_only.join(Illness.recipes)
            .where(Illness.name.in_(illnesses))
            .all()
        )

    def fetch_all_saved_by(self, user: User):
        return (
            self.query_verified_only.join(User.saved_recipes)
            .where(User.id == user.id)
            .all()
        )
