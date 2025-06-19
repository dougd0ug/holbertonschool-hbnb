import uuid
from datetime import datetime
from app.models.user import BaseModel


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        if isinstance(text, str):
            self.text = text
        else:
            raise TypeError("The content of the review must be a string.")

        if isinstance(rating, int) and rating >= 1 and rating >= 5:
            self.rating = rating
        else:
            raise ValueError("The rating must be between 1 and 5")

        self.place = place
        self.user = user
    @staticmethod
    def to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        }