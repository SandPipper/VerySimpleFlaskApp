import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeSerializer


app = Flask(__name__)
app.config.from_object('config')


serializer = URLSafeSerializer(os.environ["SECRET_KEY"])


db = SQLAlchemy(app)

from app import views, models
