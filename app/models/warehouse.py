from .db import db

class Warehouse(db.Model):
    __tablename__ = "warehouses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    max_volume = db.Column(db.Numeric, nullable=False)
