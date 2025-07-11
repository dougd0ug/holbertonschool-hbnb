import uuid
from datetime import datetime
from app.models.user import BaseModel
from app import db
from sqlalchemy.orm import relationship, validates

class Review(BaseModel):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
        "id": self.id,
        "text": self.text,
        "rating": self.rating,
        "place_id": self.place_id,
        "user_id": self.user_id
        }

    def update(self, data):
        if 'text' in data:
            if not isinstance(data['text'], str) or not data['text']:
                raise TypeError("The content of the review must be a string.")
        if 'rating' in data:
            if not isinstance(data['rating'], int) or data['rating'] < 1 or data['rating'] > 5:
                raise ValueError("The rating must be between 1 and 5")

        super().update(data)

    @validates("rating")
    def validate_rating(self, key, rating):
        if not rating or rating < 1 or self.rating > 5:
            raise ValueError("The rating must be between 1 and 5")
        else:
            return rating