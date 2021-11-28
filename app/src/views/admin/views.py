from flask_admin.contrib.sqla import ModelView
from flask_admin.model.form import InlineFormAdmin

from app.src.extensions.sqlalchemy import db
from app.src.models import Illness, Recipe, Role, User, RecipeIllness


class InlineRecipeIllnessModelForm(InlineFormAdmin):
    form_columns = ["illness_id", "recipe_id"]

    def __init__(self):
        super(InlineRecipeIllnessModelForm, self).__init__(RecipeIllness)


class RecipeView(ModelView):
    inline_models = [InlineRecipeIllnessModelForm(), ]


class IllnessView(ModelView):
    inline_models = [InlineRecipeIllnessModelForm(), ]


user_view = ModelView(User, db.session)
role_view = ModelView(Role, db.session)
recipe_view = RecipeView(Recipe, db.session)
illness_view = IllnessView(Illness, db.session)
