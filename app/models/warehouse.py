from .db import db

class Warehouse(db.Model):
    __tablename__ = "warehouses"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String, nullable=False)
    max_volume = db.Column(db.Numeric, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'city': self.city,
            'max_volume': self.max_volume
        }
