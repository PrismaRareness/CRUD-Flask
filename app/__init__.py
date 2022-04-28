from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
db.create_all()
migrate = Migrate(app, db)

from .models import client_model
from .views import client_view
