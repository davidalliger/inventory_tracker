from flask import Blueprint, render_template, redirect

from app.models import warehouse
from ..forms import ItemForm
from ..models import db, Item, Warehouse
from sqlalchemy import null


item_routes = Blueprint('items', __name__)

@item_routes.route('/')
def get_items():
    items = Item.query.order_by(Item.name).all()
    return render_template('items.html', items=items)


@item_routes.route('/', methods=["POST"])
@item_routes.route('/<int:id>', methods=["POST"])
def item(id=None):
    form = ItemForm()
    if form.validate_on_submit():
        item = Item.query.get(id) if id else Item()

        form.populate_obj(item)
        print(item)
        print(item.warehouse_id)
        if item.warehouse_id == '0':
            item.warehouse_id = null()
        print(item.warehouse_id)


        db.session.add(item)
        db.session.commit()

        return redirect(f'/items/{item.id}')
    else:
        print(form.errors)
        return render_template('item_form.html', title="Please Correct Errors", errors=form.errors, form=form)

@item_routes.route('/new')
def new_item():
    form = ItemForm()
    return render_template('item_form.html', title="Add Item", form=form, errors=None, path="/items")

@item_routes.route('/<int:id>/edit')
def edit_item(id):
    form = ItemForm()
    item = Item.query.get(id)
    form.process(obj=item)

    return render_template('item_form.html', title="Edit Item", form=form, errors=None, path=f"/items/{item.id}")

@item_routes.route('/<int:id>/delete')
def delete_item(id):
    delete_item = Item.query.get(id)

    db.session.delete(delete_item)
    db.session.commit()

    items = Item.query.order_by(Item.name).all()

    return render_template('items.html', items=items)

@item_routes.route('/<int:id>')
def item_detail(id):
    item = Item.query.get(id)
    warehouse = None
    if item.warehouse_id:
        warehouse = Warehouse.query.get(item.warehouse_id)

    return render_template('item.html', item=item, warehouse=warehouse)
