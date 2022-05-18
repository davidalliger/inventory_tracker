from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DecimalField
from wtforms.validators import DataRequired, ValidationError, AnyOf, StopValidation
from ..models import Warehouse
from .form_utils import ValidWarehouse
# from wtforms.ext.sqlalchemy.fields import QuerySelectField
# from sqlalchemy import null

def validate_name(form, field):
    name = field.data
    if len(name) < 3:
        raise ValidationError('Name must be at least three characters long.')

def validate_description(form, field):
    description = field.data
    if len(description) < 3:
        raise ValidationError('Description must be at least three characters long.')

def validate_height(form, field):
    height = field.data
    try:
        float(height)
    except:
        raise StopValidation('Height must be a number')
    if height <= 0:
        raise ValidationError('Height must be greater than zero.')

def validate_length(form, field):
    length = field.data
    try:
        float(length)
    except:
        raise StopValidation('Length must be a number')
    if length <= 0:
        raise ValidationError('Length must be greater than zero.')

def validate_width(form, field):
    width = field.data
    try:
        float(width)
    except:
        raise StopValidation('Width must be a number')
    if width <= 0:
        raise ValidationError('Width must be greater than zero.')

categories = ['Appliances', 'Cleaners', 'Decor', 'Furniture', 'Tools']

class ItemForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.warehouse_id.choices = [(0, 'Unassigned')] + [(warehouse.id, f'{warehouse.city} - #{warehouse.id}') for warehouse in Warehouse.query.order_by(Warehouse.city).all()]

    name = StringField('Name', validators=[
                                                DataRequired('Please enter a name'),
                                                validate_name
                                            ])
    category = SelectField('Category', choices=[('Appliances','Appliances'), ('Cleaners', 'Cleaners'), ('Decor', 'Decor'), ('Furniture','Furniture'), ('Tools', 'Tools')],
                                        validators=[
                                                        DataRequired('Please select a category'),
                                                        AnyOf(categories)
                                                    ])
    description = TextAreaField('Description', validators=[
                                                                DataRequired('Please enter a description'),
                                                                validate_description
                                                            ])
    height = DecimalField('Height', validators=[
                                                    validate_height
                                                ])
    length = DecimalField('Length', validators=[
                                                    validate_length
                                                ])
    width = DecimalField('Width', validators=[
                                                    validate_width
                                                ])
    warehouse_id = SelectField('Warehouse', validators=[
                                                        ValidWarehouse('height', 'length', 'width')
                                                        ])
