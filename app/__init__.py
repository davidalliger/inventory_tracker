from flask import Flask, render_template
from flask_migrate import Migrate
from .config import Config
from .routes import warehouse_routes
from .routes import item_routes
from .models import db

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(warehouse_routes, url_prefix='/warehouses')
app.register_blueprint(item_routes, url_prefix='/items')
db.init_app(app)
Migrate(app, db)


@app.route('/')
def home():
    return render_template('home.html')
