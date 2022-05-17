from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DecimalField, IntegerField
from wtforms.validators import ValidationError
from ..models import Warehouse

# def validate_city(form, field):
#     city = field.data
#     if len(city) < 3:
#         raise ValidationError('City must be at least three characters long.')

# def validate_max_volume(form, field):
#     max_volume = field.data
#     if max_volume <= 0:
#         raise ValidationError('Maximum capacity must be greater than zero.')

warehouses = Warehouse.query.order_by(Warehouse.city).all()
warehouses = [(warehouse.id, f'{warehouse.city} - #{warehouse.id}') for warehouse in warehouses]

class ItemForm(FlaskForm):
    name = StringField("Name", validators=[])
    category = SelectField("Category", choices=[('appliances','Appliances'), ('cleaners', 'Cleaners'), ('decor', 'Decor'), ('furniture','Furniture'), ('tools', 'Tools')], validators=[])
    description = TextAreaField("Description", validators=[])
    height = DecimalField("Height", validators=[])
    length = DecimalField("Length", validators=[])
    width = DecimalField("Width", validators=[])
    warehouse_id = SelectField("Warehouse", choices=[(None, "Unassigned")] + warehouses, validators=[])
