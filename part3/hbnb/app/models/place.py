import uuid
from datetime import datetime
from app.models.user import BaseModel
from app import db
from sqlalchemy.orm import relationship, validates
from sqlalchemy import Column, String, Float, DECIMAL, ForeignKey, Text, Table, Integer
from app.persistence.base import Base
from sqlalchemy.orm import mapped_column


place_amenity = db.Table(
    "place_amenity",
    Column('place_id', String(36), ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', String(36), ForeignKey('amenities.id'), primary_key=True),
)

class Place(BaseModel, Base):
    __tablename__ = 'places'

    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    owner = relationship("User", back_populates="places")

    reviews = relationship("Review", back_populates="place", lazy=True)

    amenities = relationship("Amenity", secondary=place_amenity, back_populates="places", lazy=True)

    @validates("title")
    def validate_title(self, key, title):
        if not title or len(title) > 100:
            raise ValueError("Title must be a string with 100 characters maximum.")
        else:
            return title

    @validates("price")
    def validate_price(self, key, price):
        if not price or price < 0:
            raise ValueError("Price must be over 0.")
        else:
            return price

    @validates("latitude")
    def validate_latitude(self, key, latitude):
        if not latitude or latitude < -90.0 or latitude > 90.0:
            raise ValueError("Latitude must be between -90.0 and 90.0.")
        else:
            return latitude

    @validates("longitude")
    def validate_longitude(self, key, longitude):
        if not longitude or longitude < -180.0 or longitude > 180.0:
            raise ValueError("Latitude must be between -180.0 and 180.0.")
        else:
            return longitude

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id,
            'amenities': [amenity.to_dict() for amenity in self.amenities],
            'created_at': self.created_at.isoformat() if hasattr(self, 'created_at') else None,
        }

    def update(self, data):
        if 'title' in data:
            if not isinstance(data['title'], str) or not data['title'] or len(data['title']) >= 100:
                raise ValueError("Title must be a string with 100 characters maximum.")
        if 'description' in data:
            if not isinstance(data['description'], str) or not data['description']:
                raise TypeError("Description must be a string.")
        if 'price' in data:
            if not isinstance(data['price'], (int, float)) or not data['price'] or data['price'] < 0:
                raise ValueError("Price must be over 0.")
        if 'latitude' in data:
            if not isinstance(data['latitude'], (int, float)) or not data['latitude'] or data['latitude'] <= -90.0 or data['latitude'] >= 90.0:
                raise ValueError("Latitude must be between -90.0 and 90.0.")
        if 'longitude' in data:
            if not isinstance(data['longitude'], (int, float)) or not data['longitude'] or data['longitude'] <= -180.0 or data['longitude'] >= 180.0:
                raise ValueError("Latitude must be between -180.0 and 180.0.")

        super().update(data)
