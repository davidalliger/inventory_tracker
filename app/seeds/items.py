from ..models import db, Item
from sqlalchemy import null

def seed_items():
    item1 = Item(name='Couch', category='Furniture', description='It is very comfortable!', height=3, length=7, width=4, warehouse_id=1)
    item2 = Item(name='Painting', category='Decor', description='A painting of a cow in a field', height=2, length=3, width=0.1, warehouse_id=3)
    item3 = Item(name='Vase', category='Decor', description='A blue ceramic vase', height=1, length=0.5, width=0.5, warehouse_id=4)
    item4 = Item(name='Washing Machine', category='Appliances', description='A sturdy washing machine', height=3, length=3, width=3, warehouse_id=5)
    item5 = Item(name='Hammer', category='Tools', description='A trusty hammer', height=0.7, length=0.2, width=0.1, warehouse_id=null())
    item6 = Item(name='Detergent', category='Cleaners', description='A bottle of detergent', height=1, length=.6, width=.2, warehouse_id=9)
    item7 = Item(name='Refrigerator', category='Appliances', description='A big refrigerator', height=7, length=3.5, width=3, warehouse_id=7)
    item8 = Item(name='Blender', category='Appliances', description='It will blend your food!', height=0.7, length=0.4, width=0.4, warehouse_id=8)
    item9 = Item(name='Bed', category='Furniture', description='You will sleep so well!', height=2, length=7, width=4, warehouse_id=2)
    item10 = Item(name='Wall Clock', category='Appliances', description='What time is it?', height=.6, length=.6, width=.1, warehouse_id=6)

    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.add(item4)
    db.session.add(item5)
    db.session.add(item6)
    db.session.add(item7)
    db.session.add(item8)
    db.session.add(item9)
    db.session.add(item10)

    db.session.commit()

# Use raw SQL to empty the table, reset the identity, and delete dependent entries
def undo_items():
    db.session.execute('TRUNCATE items RESTART IDENTITY CASCADE;')
    db.session.commit()
