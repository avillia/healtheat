from app.src.extensions.sqlalchemy import db
from app.src.helpers.enums import Roles as RoleEnum
from app.src.models.main import BaseModel


class Role(BaseModel):
    __tablename__ = "user_roles"

    name = db.Column(db.Enum(RoleEnum), primary_key=True)
    can_manage_users_data = db.Column(db.Boolean)
    can_manage_medical_info = db.Column(db.Boolean)

    users = db.relationship("User", back_populates="role")
