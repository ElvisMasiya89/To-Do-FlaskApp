import unittest
from unittest.mock import Mock, patch
from ..app import app


class FrontendTestCase(unittest.TestCase):

    @patch('requests.post')
    def test_create_todo(self, mock_post):
        mock_post.return_value.status_code = 200  # Simulate a successful response
        with app.test_client() as client:
            response = client.post('/create_todo', data={'title': 'Test Todo', 'description': 'Test Description',
                                                         'due_date': '2023-12-31'})
            self.assertEqual(response.status_code, 302)  # Should redirect to index



if __name__ == '__main__':
    unittest.main()
