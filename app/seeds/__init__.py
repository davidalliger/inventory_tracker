from flask.cli import AppGroup
from .warehouses import seed_warehouses, undo_warehouses
from .items import seed_items, undo_items

seed_commands = AppGroup('seed')

@seed_commands.command('all')
def seed():
    seed_warehouses()
    seed_items()

@seed_commands.command('undo')
def undo():
    undo_warehouses()
    undo_items()
