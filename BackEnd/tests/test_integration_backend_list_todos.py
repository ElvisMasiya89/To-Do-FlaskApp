import os
import unittest
from ..app import app, db, ToDoItem


class BackendTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use an SQLite in-memory database for testing

        with app.app_context():
            # Create the database tables
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_list_todos(self):
        with app.test_client() as client:
            # Create a test todo item in the database
            todo = ToDoItem(title='Test Todo', description='Test Description', due_date='2023-12-31')
            with app.app_context():
                db.session.add(todo)
                db.session.commit()

            response = client.get('/todos')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Test Todo', response.data)


if __name__ == '__main__':
    unittest.main()
