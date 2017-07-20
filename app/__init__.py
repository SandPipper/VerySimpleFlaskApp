import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from itsdangerous import URLSafeSerializer


app = Flask(__name__)
app.config.from_object('config')

serializer = URLSafeSerializer(os.environ["SECRET_KEY"])


db = SQLAlchemy(app)

query_cache = {}
mysql_engine = create_engine("mysql+pymysql://{}:{}@localhost/?charset=utf8mb4"\
                            .format(os.environ['USER'],
                                    os.environ['PASSWORD']),
                             execution_options={'compiled_cache': query_cache})

mysql_engine.execute("CREATE DATABASE IF NOT EXISTS {} \
                     CHARACTER SET utf8 COLLATE utf8_unicode_ci" \
                     .format(os.environ['DB_NAME']))
mysql_engine.execute("USE {}".format(os.environ['DB_NAME']))

from .models import Person

db.create_all()
db.session.commit()

from app import views, models
