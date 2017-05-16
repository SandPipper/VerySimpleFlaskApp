from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import app, db
import os

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
