from flask import Blueprint
from app.forms.warehouse import WarehouseForm


warehouse_routes = Blueprint('warehouses', __name__)

@warehouse_routes.route('/warehouses', methods=["POST"])
def create_warehouse():
    form = WarehouseForm()
    if form.validate_on_submit():
        return 'Cool.'
