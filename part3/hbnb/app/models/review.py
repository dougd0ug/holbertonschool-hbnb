import uuid
from datetime import datetime
from app.models.user import BaseModel
from app import db
from sqlalchemy.orm import relationship, validates
from sqlalchemy import Column, Integer, String, ForeignKey
from app.persistence.base import Base

class Review(BaseModel, Base):
    __tablename__ = 'reviews'

    text = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    place = relationship("Place", back_populates="reviews")
    user = relationship("User", back_populates="reviews")

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
        rating = data.get('rating')
        if rating is None:
            raise ValueError("Rating is required")
        if not isinstance(rating, int):
            raise ValueError("Rating must be an integer")
        if rating < 1 or rating > 5:
            raise ValueError("The rating must be between 1 and 5")

        super().update(data)

    @validates("rating")
    def validate_rating(self, key, rating):
        if rating is None or rating < 1 or rating > 5:
            raise ValueError("The rating must be between 1 and 5")
        return rating
