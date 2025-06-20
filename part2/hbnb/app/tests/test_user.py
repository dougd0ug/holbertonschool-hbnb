import unittest
from app.models.user import User
from app import create_app

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User(
            first_name="Alice",
            last_name="Smith",
            email="alice@example.com",
            is_admin=True
        )

    def test_valid_user_initialization(self):
        self.assertEqual(self.user.first_name, "Alice")
        self.assertEqual(self.user.last_name, "Smith")
        self.assertEqual(self.user.email, "alice@example.com")
        self.assertTrue(self.user.is_admin)
        self.assertIsNotNone(self.user.id)
        self.assertIsNotNone(self.user.created_at)
        self.assertIsInstance(self.user.places, list)

    def test_invalid_first_name(self):
        with self.assertRaises(ValueError):
            User("", "Doe", "test@example.com")

    def test_invalid_last_name(self):
        with self.assertRaises(ValueError):
            User("John", "", "test@example.com")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            User("John", "Doe", "not-an-email")

    def test_invalid_is_admin_type(self):
        with self.assertRaises(TypeError):
            User("Jane", "Doe", "jane@example.com", is_admin="yes")

    def test_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["first_name"], "Alice")
        self.assertEqual(user_dict["email"], "alice@example.com")
        self.assertIn("id", user_dict)

    def test_owns_place(self):
        dummy_place = object()
        self.user.owns_place(dummy_place)
        self.assertIn(dummy_place, self.user.places)


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
            "first_name": "Caroline",
            "last_name": "White",
            "email": "carol.white@example.com"
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
