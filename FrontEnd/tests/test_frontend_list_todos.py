import unittest
from ..app import app


class FrontendTestCase(unittest.TestCase):

    def test_list_todos(self):
        with app.test_client() as client:
            response = client.get('/todos')
            self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
