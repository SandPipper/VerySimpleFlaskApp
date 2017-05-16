from app import app, db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    surname = db.Column(db.String(20))

    def __init__(self, first_name, surname, **kwargs):
        db.Model.__init__(self, first_name=first_name, surname=surname, **kwargs)

    def __repr__(self):
        return '<Person %r, %r' % (self.surname, self.first_name)
