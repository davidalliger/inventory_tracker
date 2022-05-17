from .db import db

class Warehouse(db.Model):
    __tablename__ = "warehouses"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String, nullable=False)
    max_volume = db.Column(db.Numeric, nullable=False)
