from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from sqlalchemy import create_engine
from app import app, db
from app.models import Person
import os

query_cache = {}
mysql_engine = create_engine("mysql+pymysql://{}:{}@localhost/?charset=utf8mb4"\
                            .format(os.environ['USER'],
                                    os.environ['PASSWORD']),
                             execution_options={'compiled_cache': query_cache})

mysql_engine.execute("CREATE DATABASE IF NOT EXISTS {} \
                     CHARACTER SET utf8 COLLATE utf8_unicode_ci" \
                     .format(os.environ['DB_NAME']))
                     
mysql_engine.execute("USE {}".format(os.environ['DB_NAME']))


db.create_all()
db.session.commit()

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@localhost/{}?charset=utf8mb4"\
                          .format(os.environ['USER'],
                                  os.environ['PASSWORD'],
                                  os.environ['DB_NAME'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
