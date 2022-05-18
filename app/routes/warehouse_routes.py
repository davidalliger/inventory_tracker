from flask import Blueprint, render_template, request, redirect
from ..forms import WarehouseForm
from ..models import Warehouse, db


warehouse_routes = Blueprint('warehouses', __name__)


@warehouse_routes.route('/')
def get_warehouses():
    warehouses = Warehouse.query.order_by(Warehouse.city).all()
    return render_template('warehouses.html', warehouses=warehouses)


@warehouse_routes.route('/', methods=["POST"])
@warehouse_routes.route('/<int:id>', methods=["POST"])
def warehouse(id=None):
    form = WarehouseForm()
    if form.validate_on_submit():
        warehouse = Warehouse.query.get(id) if id else Warehouse()
        form.populate_obj(warehouse)

        db.session.add(warehouse)
        db.session.commit()

        return redirect(f'/warehouses/{warehouse.id}')
    else:
        print(form.errors)
        return render_template('warehouse_form.html', title="Please Correct Errors", errors=form.errors, form=form)

@warehouse_routes.route('/new')
def new_warehouse():
    form = WarehouseForm()
    return render_template('warehouse_form.html', title="Add Warehouse", form=form, errors=None, path="/warehouses")

@warehouse_routes.route('/<int:id>/edit')
def edit_warehouse(id):
    form = WarehouseForm()
    warehouse = Warehouse.query.get(id)
    form.process(obj=warehouse)

    return render_template('warehouse_form.html', title="Edit Warehouse", form=form, errors=None, path=f"/warehouses/{warehouse.id}")

@warehouse_routes.route('/<int:id>/delete')
def delete_warehouse(id):
    delete_warehouse = Warehouse.query.get(id)

    db.session.delete(delete_warehouse)
    db.session.commit()

    warehouses = Warehouse.query.order_by(Warehouse.city).all()

    return render_template('warehouses.html', warehouses=warehouses)

@warehouse_routes.route('/<int:id>')
def warehouse_detail(id):
    warehouse = Warehouse.query.get(id)
    inventory = None
    if len(warehouse.inventory) > 0:
        inventory = warehouse.inventory

    return render_template('warehouse.html', warehouse=warehouse, inventory=inventory)
