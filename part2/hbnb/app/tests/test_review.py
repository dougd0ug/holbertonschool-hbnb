import unittest
from app.models.review import Review
from datetime import datetime

class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review(
            text="Great view and good food!",
            rating=5,
            place_id="place123",
            user_id="user456"
        )

    def test_valid_initialization(self):
        self.assertEqual(self.review.text, "Great view and good food!")
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.place_id, "place123")
        self.assertEqual(self.review.user_id, "user456")
        self.assertIsNotNone(self.review.id)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_invalid_text_type(self):
        with self.assertRaises(TypeError):
            Review(text=123, rating=4, place_id="p1", user_id="u1")

    def test_invalid_rating_value(self):
        with self.assertRaises(ValueError):
            Review(text="Nice", rating=0, place_id="p1", user_id="u1")
        with self.assertRaises(ValueError):
            Review(text="Nice", rating=6, place_id="p1", user_id="u1")

    def test_to_dict(self):
        d = self.review.to_dict()
        self.assertEqual(d['text'], "Great place!")
        self.assertEqual(d['rating'], 5)
        self.assertEqual(d['place_id'], "place123")
        self.assertEqual(d['user_id'], "user456")
        self.assertIn('id', d)

    def test_update_review(self):
        old_updated_at = self.review.updated_at
        self.review.update({'text': "Updated review", 'rating': 4})
        self.assertEqual(self.review.text, "Updated review")
        self.assertEqual(self.review.rating, 4)
        self.assertNotEqual(self.review.updated_at, old_updated_at)

if __name__ == "__main__":
    unittest.main()
