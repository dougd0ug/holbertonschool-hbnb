import unittest
from app.models.user import User

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

if __name__ == '__main__':
    unittest.main()
