from flask import Blueprint
from app.forms.warehouse import Warehouse, WarehouseForm

@app.route('/warehouses')
def create_warehouse():
    form = WarehouseForm()
