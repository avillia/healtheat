"""
In order to create new model:
1. Create new module for it;
2. Implement its Manager (derive from .main.BaseManager);
3. Describe Model (derive from .main.BaseModel) and pass Manager to it;
4. Don't forget to import new model here.
"""

from .associative import RecipeIllness, SavedRecipes, UserIllness
from .illness import Illness
from .recipe import Recipe
from .role import Role
from .user import User
