from flask import render_template, session, url_for, request
from .forms import Add_personForm
from .models import Person
from app import app

@app.route('/')
@app.route('/index')
def index(title="Index page"):
    person = Person.query.all()
    return render_template('index.html', person=person, title=title)

@app.route('/new_person')
def new_person(title="New Person Creation"):
    form = Add_personForm(request.form)
    return render_template('add_new_person.html', form=form, title=title)

#Some addition
@app.route("/get_data")
def get_data(title="Some tests JQuery"):
    return render_template('get_data.html', title=title)

@app.errorhandler(404)
def not_found_error(error, title="Not found"):
    return render_template('404.html', title=title), 404
