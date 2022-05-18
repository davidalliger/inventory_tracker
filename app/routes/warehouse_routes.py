from flask import Blueprint, render_template, request, redirect
from ..forms import WarehouseForm
from ..models import Warehouse, db
from sqlalchemy import null


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
        space_occupied = 0
        for item in warehouse.inventory:
            space_occupied += (item.height * item.width * item.length)
        form.populate_obj(warehouse)
        if warehouse.max_volume < space_occupied:
            errors={'max_volume': ['Warehouse cannot be smaller than items inside! Please adjust maximum capacity.']}
            return render_template('warehouse_form.html', title="Please Correct Errors", errors=errors, form=form)

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
    for item in delete_warehouse.inventory:
        item.warehouse_id = null()
        # db.session.save()
    db.session.delete(delete_warehouse)
    db.session.commit()

    warehouses = Warehouse.query.order_by(Warehouse.city).all()

    return render_template('warehouses.html', warehouses=warehouses)

@warehouse_routes.route('/<int:id>')
def warehouse_detail(id):
    warehouse = Warehouse.query.get(id)
    inventory = None
    current_capacity = warehouse.max_volume
    if len(warehouse.inventory) > 0:
        inventory = warehouse.inventory
        for item in inventory:
            current_capacity -= item.height * item.width * item.length

    return render_template('warehouse.html', warehouse=warehouse, inventory=inventory, current_capacity=current_capacity)
