from flask import Blueprint, render_template
from app.forms.warehouse import WarehouseForm
from ..models import Warehouse


warehouse_routes = Blueprint('warehouses', __name__)

@warehouse_routes.route('/warehouses')
def get_warehouses():
    warehouses = Warehouse.query.order_by(Warehouse.city).all()
    return render_template('warehouses.html', warehouses)


@warehouse_routes.route('/warehouses', methods=["POST"])
def create_warehouse():
    form = WarehouseForm()
    if form.validate_on_submit():
        return 'Cool.'
