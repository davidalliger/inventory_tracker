from wtforms import ValidationError
from wtforms.validators import StopValidation

from app.models import warehouse
from ..models import Warehouse


class ValidWarehouse(object):
    """
    Checks to see if item will fit inside warehouse

    """
    def __init__(self, height, length, width):
        self.height = height
        self.length = length
        self.width = width

    def __call__(self, form, field):
        if field.data == '0':
            raise StopValidation()
        height = form[self.height]
        length = form[self.length]
        width = form[self.width]
        if not height.data or not length.data or not width.data:
            raise StopValidation()
        warehouse = Warehouse.query.get(field.data)
        current_capacity = warehouse.max_volume
        print(current_capacity)
        print(warehouse.inventory)
        for item in warehouse.inventory:
            current_capacity -= (item.height * item.length * item.width)
        volume = height.data * length.data * width.data
        print(volume)
        if current_capacity < volume:
            raise ValidationError('This item will not fit in the selected warehouse. Remove items from the warehouse first and then try again.')
