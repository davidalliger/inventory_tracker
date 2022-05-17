from flask import Blueprint, render_template, request
from app.forms.warehouse import WarehouseForm
from ..models import Warehouse, db


warehouse_routes = Blueprint('warehouses', __name__)


@warehouse_routes.route('/')
def get_warehouses():
    warehouses = Warehouse.query.order_by(Warehouse.city).all()
    return render_template('warehouses.html', warehouses=warehouses)


@warehouse_routes.route('/', methods=["POST"])
def create_warehouse():
    form = WarehouseForm()
    form['csrf_token'].data = request.cookies['crsf_token']
    if form.validate_on_submit():
        new_warehouse = Warehouse()
        form.populate_obj(new_warehouse)

        db.session.add(new_warehouse)
        db.session.commit()

        return render_template('warehouse.html', id=new_warehouse.id)

@warehouse_routes.route('/new')
def new_warehouse():
    form = WarehouseForm()
    return render_template('warehouse_form.html', form=form)

@warehouse_routes.route('/<int:id>/edit')
def edit_warehouse(id):
    form = WarehouseForm()
    warehouse = Warehouse.query.get(id)
    form.process(obj=warehouse)

    return render_template('warehouse_form.html', form=form)

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

    return render_template('warehouse.html', warehouse=warehouse)
