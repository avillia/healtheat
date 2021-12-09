"""
Created for resolving circular import error.
Also describes sample structure for every new model.
"""

from app.src.extensions.sqlalchemy import db


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {"extend_existing": True}
