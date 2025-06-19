import uuid
from datetime import datetime
from app.models.user import BaseModel


class Review(BaseModel):
    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        if text and isinstance(text, str):
            self.text = text
        else:
            raise TypeError("The content of the review must be a string.")

        if isinstance(rating, int) and rating >= 1 and rating <= 5:
            self.rating = rating
        else:
            raise ValueError("The rating must be between 1 and 5")

        self.place_id = place_id
        self.user_id = user_id


    def to_dict(self):
        return {
        "id": self.id,
        "text": self.text,
        "rating": self.rating,
        "place_id": self.place_id,
        "user_id": self.user_id
        }
