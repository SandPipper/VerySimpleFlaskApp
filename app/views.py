from flask import render_template, session, url_for, request, jsonify
from .forms import Add_personForm
from .models import Person
from app import app, db, serializer


@app.route('/')
@app.route('/index')
def index(title="Index page"):
    persons = Person.query.all()
    for person in persons:
        person.id = serializer.dumps(person.id)
    return render_template('index.html', persons=persons, title=title)


@app.route('/new_person')
def new_person(title="New Person Creation"):
    form = Add_personForm(request.form)
    return render_template('add_new_person.html', form=form, title=title)


@app.errorhandler(404)
def not_found_error(error, title="Not found"):
    return render_template('404.html', title=title), 404


@app.route('/new_person/', methods=['POST'])
def add_new_person():

    form = Add_personForm(request.form)
    data = {'status': 0, 'message': 'Validate Fail'}

    if form.validate_on_submit() and request.method == 'POST':
        person = Person(first_name=request.form['first_name'],
                        surname=request.form['surname'])
        db.session.add(person)
        db.session.commit()
        data = {'status': 1, 'message': 'Person Added'}

    return jsonify(data)


@app.route('/delete/<person_id>', methods=['DELETE'])
def delete_person(person_id):
    result = {'status': 0, 'message': 'Error'}

    try:
        person_id = serializer.loads(person_id)
        db.session.query(Person).filter_by(id=person_id).delete()
        db.session.commit()
        result = {'status': 1, 'message': 'Person Deleted'}

    except Exception as e:
        print(e, repr(e))
        result = {'status': 0, 'message': repr(e)}

    return jsonify(result)
