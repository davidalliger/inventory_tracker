from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DecimalField
from wtforms.validators import ValidationError
from ..models import Warehouse
# from wtforms.ext.sqlalchemy.fields import QuerySelectField
# from sqlalchemy import null

# def validate_city(form, field):
#     city = field.data
#     if len(city) < 3:
#         raise ValidationError('City must be at least three characters long.')

# def validate_max_volume(form, field):
#     max_volume = field.data
#     if max_volume <= 0:
#         raise ValidationError('Maximum capacity must be greater than zero.')

class ItemForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.warehouse_id.choices = [(0, "Unassigned")] + [(warehouse.id, f'{warehouse.city} - #{warehouse.id}') for warehouse in Warehouse.query.order_by(Warehouse.city).all()]

    name = StringField("Name")
    category = SelectField("Category", choices=[('Appliances','Appliances'), ('Cleaners', 'Cleaners'), ('Decor', 'Decor'), ('Furniture','Furniture'), ('Tools', 'Tools')])
    description = TextAreaField("Description")
    height = DecimalField("Height")
    length = DecimalField("Length")
    width = DecimalField("Width")
    warehouse_id = SelectField("Warehouse")
