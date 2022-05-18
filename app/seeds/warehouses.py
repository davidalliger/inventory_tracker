from ..models import db, Warehouse

def seed_warehouses():
    warehouse1 = Warehouse(city='Atlanta', max_volume='1000')
    warehouse2 = Warehouse(city='Houston', max_volume='5000')
    warehouse3 = Warehouse(city='Los Angeles', max_volume='5000')
    warehouse4 = Warehouse(city='San Antonio', max_volume='1000')
    warehouse5 = Warehouse(city='Seattle', max_volume='3000')
    warehouse6 = Warehouse(city='Tacoma', max_volume='1000')
    warehouse7 = Warehouse(city='Los Angeles', max_volume='1000')
    warehouse8 = Warehouse(city='Atlanta', max_volume='1000')
    warehouse9 = Warehouse(city='Boston', max_volume='500')
    warehouse10 = Warehouse(city='Tucson', max_volume='1000')

    db.session.add(warehouse1)
    db.session.add(warehouse2)
    db.session.add(warehouse3)
    db.session.add(warehouse4)
    db.session.add(warehouse5)
    db.session.add(warehouse6)
    db.session.add(warehouse7)
    db.session.add(warehouse8)
    db.session.add(warehouse9)
    db.session.add(warehouse10)

    db.session.commit()

# Use raw SQL to empty the table, reset the identity, and delete dependent entries
def undo_warehouses():
    db.session.execute('TRUNCATE warehouses RESTART IDENTITY CASCADE;')
    db.session.commit()
