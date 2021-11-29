"""
Created for resolving circular import error.
Also describes sample structure for every new model.
"""

from flask_sqlalchemy import BaseQuery

from app.src.extensions.sqlalchemy import db


class BaseManager(BaseQuery):
    @property
    def model(self):
        return self._propagate_attrs["plugin_subject"].entity


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {'extend_existing': True}

    query_class = BaseManager
