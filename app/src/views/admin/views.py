from flask_admin.contrib.sqla import ModelView

from app.configs.extensions import db
from app.src.models import Illness, Recipe, Role, User


class RecipeView(ModelView):
    column_hide_backrefs = False


class IllnessView(ModelView):
    column_hide_backrefs = False


user_view = ModelView(User, db.session)
role_view = ModelView(Role, db.session)
recipe_view = RecipeView(Recipe, db.session)
illness_view = IllnessView(Illness, db.session)

views = [
    user_view,
    role_view,
    recipe_view,
    illness_view,
]
