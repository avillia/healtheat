from flask_sqlalchemy import BaseQuery

from .main import Illness


class BaseManager(BaseQuery):
    @property
    def model(self):
        return self._propagate_attrs["plugin_subject"].entity


class UserManager(BaseManager):
    pass


class IllnessManager(BaseManager):
    pass


class RecipeManager(BaseManager):

    @property
    def verified_only(self):
        return self.filter_by(is_verified=True)

    def fetch_all_verified(self):
        return self.verified_only.all()

    def fetch_all_related_to_illness(self, illness: Illness):
        return self.verified_only.join(Illness.recipes).where(Illness.id == illness.id).all()

