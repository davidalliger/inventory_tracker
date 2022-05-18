from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.validators import ValidationError, StopValidation
from ..models import Warehouse

def validate_city(form, field):
    city = field.data
    if len(city) < 3:
        raise ValidationError('City must be at least three characters long.')

def validate_max_volume(form, field):
    max_volume = field.data
    try:
        float(max_volume)
    except:
        raise StopValidation('Maximum capacity must be a number')
    if max_volume <= 0:
        raise ValidationError('Maximum capacity must be greater than zero.')

class WarehouseForm(FlaskForm):
    city = StringField("City", validators=[
                                            validate_city
                                            ])
    max_volume = DecimalField("Maximum Volume", validators=[
                                                            validate_max_volume
                                                            ])
