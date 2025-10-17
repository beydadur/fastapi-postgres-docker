import datetime as _dt
import sqlalchemy as _sql
from . import db as _database

class Item(_database.Base):
    __tablename__ = "items"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    title = _sql.Column(_sql.String, index=True)
    description = _sql.Column(_sql.String, index=True)
    price = _sql.Column(_sql.Float, index=True)
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
