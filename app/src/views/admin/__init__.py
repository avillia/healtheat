from app.configs.extensions import admin

from .views import views

admin_bp = admin

for view in views:
    admin_bp.add_view(view)
