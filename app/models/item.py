from sqlalchemy import ForeignKey
from .db import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouses.id"), nullable=False)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    volume = db.Column(db.Numeric, nullable=False)

    warehouse = db.relationship("Warehouse")
