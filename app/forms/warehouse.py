from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField


class WarehouseForm(FlaskForm):
    name = StringField("Name")
    city = StringField("City")
    max_volume = DecimalField("Maximum Volume")
