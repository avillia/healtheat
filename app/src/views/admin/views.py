from flask_admin.contrib.sqla import ModelView

from app.src.extensions.sqlalchemy import db
from app.src.models import Illness, Recipe, Role, User


class RecipeView(ModelView):
    pass


class IllnessView(ModelView):
    pass


user_view = ModelView(User, db.session)
role_view = ModelView(Role, db.session)
recipe_view = RecipeView(Recipe, db.session)
illness_view = IllnessView(Illness, db.session)
