from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__, template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///librasic.db'
app.config.from_file('envconfig.json', load=json.load)

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
migrate = Migrate(app, db)

global ENV_VARS
ENV_VARS={}
DEFAULT_RENT_FEE = {'DEFAULT_RENT_FEE': int(app.config['DEFAULT_RENT_FEE'])}
ENV_VARS.update(DEFAULT_RENT_FEE)

from librasic.modules import routes