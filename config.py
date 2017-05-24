import os
from itsdangerous import URLSafeSerializer

serializer = URLSafeSerializer(os.environ['SECRET_KEY'])

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SECRET_KEY = serializer.dumps(os.environ['SECRET_KEY'])
