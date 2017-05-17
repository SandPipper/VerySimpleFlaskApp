import unittest
from app import app, db
from app.models import Person


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_add_user(self):
        tester = Person(first_name="Unit", surname="Test")
        db.session.add(tester)
        db.session.commit()
        self.assertEqual(str(db.session.query(Person).filter_by(
            first_name="Unit").first()), "<Person 'Test', 'Unit'")

    def test_delete_person(self):
        db.session.query(Person).filter_by(first_name="Unit").delete()
        db.session.commit()
        self.assertEqual(str(db.session.query(Person).filter_by(
            first_name="Unit").first()), "None")

if __name__ == "__main__":
    unittest.main()
