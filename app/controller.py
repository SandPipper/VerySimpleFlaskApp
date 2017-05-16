from flask import jsonify, session, request
from .forms import Add_personForm
from .models import Person
from app import app, db

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
        #person = Person.query.get(persons_id) /* too slow implemented
        #db.session.delete(person) */
        db.session.commit()
        result = {'status': 1, 'message': 'Person Deleted'}
    except Exception as e:
        print(repr(e))
        result = {'status': 0, 'message': repr(e)}

    return jsonify(result)

@app.route("/echo/", methods=['GET'])
def echo():
    ret_data = {"value": request.args.get('echoValue')}
    return jsonify(ret_data)

@app.route("/_add_numbers")
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result = a + b)
