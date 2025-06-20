import unittest
from app.api import create_app

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_data(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)

    def test_get_all_users(self):
        # Create a user first
        self.client.post('/api/v1/users/', json={
            "first_name": "Alice",
            "last_name": "Smith",
            "email": "alice.smith@example.com"
        })
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_update_user(self):
        # Create a user
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Carol",
            "last_name": "White",
            "email": "carol.white@example.com"
        })
        user_id = response.get_json().get("id")
        # Update the user
        response = self.client.put(f'/api/v1/users/{user_id}', json={
            "first_name": "Caroline"
        })
        self.assertEqual(response.status_code, 200)

    def test_create_user_missing_fields(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Eve"
            # Missing last_name and email
        })
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()