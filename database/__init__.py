from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from ItIsTasty import app
from ItIsTasty.loader import model_load

import os
DB_NAME = os.environ['DAPP_DB_NAME']
DB_USER = os.environ['DAPP_DB_USER']
DB_PASSWORD = os.environ['DAPP_DB_PASSWORD']
DB_ADDRESS = os.environ['DAPP_DB_ADDRESS']

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql+pymysql://{}:{}@{}/{}?charset=utf8'\
    .format(DB_USER, DB_PASSWORD, DB_ADDRESS, DB_NAME)

DB = SQLAlchemy(app)
migrate = Migrate(app, DB, compare_type=True)

model_load(
    'test',
    'user'
)