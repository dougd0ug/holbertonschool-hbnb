import unittest
from place import Place
import uuid

class TestPlace(unittest.TestCase):

    def setUp(self):
        # Valeurs valides de base
        self.valid_data = {
            "title": "Nice apartment",
            "description": "A lovely place in Paris.",
            "price": 120.0,
            "latitude": 48.8566,
            "longitude": 2.3522,
            "owner_id": str(uuid.uuid4()),  # simulons un ID de user
            "amenities": []
        }

    def test_create_valid_place(self):
        place = Place(**self.valid_data)
        self.assertEqual(place.title, self.valid_data["title"])
        self.assertEqual(place.price, self.valid_data["price"])
        self.assertEqual(place.latitude, self.valid_data["latitude"])

    def test_title_too_long(self):
        data = self.valid_data.copy()
        data["title"] = "A" * 101  # 101 caractères
        with self.assertRaises(ValueError):
            Place(**data)

    def test_price_negative(self):
        data = self.valid_data.copy()
        data["price"] = -50.0
        with self.assertRaises(ValueError):
            Place(**data)

    def test_invalid_latitude(self):
        data = self.valid_data.copy()
        data["latitude"] = 150.0
        with self.assertRaises(ValueError):
            Place(**data)

    def test_invalid_longitude(self):
        data = self.valid_data.copy()
        data["longitude"] = -200.0
        with self.assertRaises(ValueError):
            Place(**data)

    def test_to_dict_output(self):
        place = Place(**self.valid_data)
        result = place.to_dict()
        self.assertIn("title", result)
        self.assertIn("latitude", result)
        self.assertIn("owner_id", result)
