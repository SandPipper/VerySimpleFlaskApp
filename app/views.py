from flask import render_template, session, url_for, request, jsonify
from .forms import Add_personForm
from .models import Person
from app import app, db


@app.route('/')
@app.route('/index')
def index(title="Index page"):
    person = Person.query.all()
    return render_template('index.html', person=person, title=title)


@app.route('/new_person')
def new_person(title="New Person Creation"):
    form = Add_personForm(request.form)
    return render_template('add_new_person.html', form=form, title=title)


@app.errorhandler(404)
def not_found_error(error, title="Not found"):
    return render_template('404.html', title=title), 404


@app.route('/new_person/', methods=['POST'])
def add_new_person():
    data = {'status': 0}
    form = Add_personForm(request.form)
    if form.validate_on_submit() and request.method == 'POST':
        person = Person(first_name=request.form['first_name'],
                        surname=request.form['surname'])
        db.session.add(person)
        db.session.commit()
        data = {'status': 1}
    return jsonify(data)


@app.route('/delete/<persons_id>', methods=['DELETE'])
def delete_person(persons_id):
    result = {'status': 0, 'message': 'Error'}
    try:
        db.session.query(Person).filter_by(id=persons_id).delete()
        db.session.commit()
        result = {'status': 1, 'message': 'Person Deleted'}
    except Exception as e:
        print(repr(e))
        result = {'status': 0, 'message': repr(e)}

    return jsonify(result)
