from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = "9988"
app.config['JWT_ALGORITHM'] = "LoK45"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lab4_o48r_user:Fp7eRIsFgmki5shwcbnCoHm0pEjd1FBv@dpg-cmc3vnmn7f5s7396b1pg-a.oregon-postgres.render.com/lab4_o48r"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

import lab2.views
import lab2.models
