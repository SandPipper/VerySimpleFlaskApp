import unittest
import json
from app import app, db, serializer
from app.models import Person


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_add_person(self):
        tester = app.test_client(self)
        response = tester.post('/new_person/', data=dict(first_name="Unit",
                                                         surname="Test"))
        data = json.loads((response.data).decode('utf-8'))
        self.assertEqual(data['status'], 1)

    def test_delete_person(self):
        with app.app_context():
            person = Person.query.filter_by(first_name="Unit").first()
            person_id = serializer.dumps(person.id)
            tester = app.test_client(self)
            response = tester.delete('/delete/' + person_id)
            data = json.loads((response.data).decode('utf-8'))
        self.assertEqual(data['status'], 1)

if __name__ == "__main__":
    unittest.main()
