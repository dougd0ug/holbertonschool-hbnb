import unittest
from app.models.amenity import Amenity
from datetime import datetime

class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity("Wi-Fi")

    def test_initialization(self):
        self.assertEqual(self.amenity.name, "Wi-Fi")
        self.assertIsNotNone(self.amenity.id)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_invalid_name_type(self):
        with self.assertRaises(TypeError):
            Amenity(123)

    def test_missing_name(self):
        with self.assertRaises(TypeError):
            Amenity(None)

    def test_to_dict(self):
        amenity_dict = self.amenity.to_dict()
        self.assertIn("id", amenity_dict)
        self.assertEqual(amenity_dict["name"], "Wi-Fi")

    def test_update_name(self):
        old_updated_at = self.amenity.updated_at
        self.amenity.update({"name": "Parking"})
        self.assertEqual(self.amenity.name, "Parking")
        self.assertNotEqual(self.amenity.updated_at, old_updated_at)

if __name__ == "__main__":
    unittest.main()
