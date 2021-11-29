from flask_admin.contrib.sqla import ModelView

from app.src.extensions.sqlalchemy import db
from app.src.models import Illness, Recipe, Role, User


class IllnessView(ModelView):
    pass


class RecipeView(ModelView):
    pass


class RoleView(ModelView):
    pass


class UserView(ModelView):
    pass


illness_view = IllnessView(Illness, db.session)
recipe_view = RecipeView(Recipe, db.session)
role_view = RoleView(Role, db.session)
user_view = UserView(User, db.session)
