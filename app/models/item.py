from sqlalchemy import ForeignKey
from .db import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouses.id"), nullable=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    height = db.Column(db.Numeric, nullable=False)
    length = db.Column(db.Numeric, nullable=False)
    width = db.Column(db.Numeric, nullable=False)
    description = db.Column(db.String, nullable=False)

    warehouse = db.relationship("Warehouse", back_populates='inventory')
