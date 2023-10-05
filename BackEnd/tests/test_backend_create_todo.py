import unittest
from ..app import app, db, ToDoItem


class BackendTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use an SQLite in-memory database for testing
        with app.app_context():
             db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_todo(self):
        with app.test_client() as client:
            data = {'title': 'Test Todo', 'description': 'Test Description', 'due_date': '2023-12-31'}
            response = client.post('/todo', json=data)
            self.assertEqual(response.status_code, 200)
            todo = ToDoItem.query.first()
            self.assertIsNotNone(todo)
            self.assertEqual(todo.title, 'Test Todo')


if __name__ == '__main__':
    unittest.main()
