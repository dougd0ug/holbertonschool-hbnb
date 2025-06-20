import uuid
from datetime import datetime
from app.models.user import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities):
        super().__init__()

        if title and len(title) <= 100 and isinstance(title, str):
            self.title = title
        else:
            raise ValueError("Title must be a string with 100 characters maximum.")

        if description and isinstance(description, str):
            self.description = description
        else:
            raise TypeError("Description must be a string.")

        if price and price > 0 and isinstance(price, (int, float)):
            self.price = price
        else:
            raise ValueError("Price must be over 0.")

        if latitude and isinstance(latitude, (int, float)) and latitude >= -90.0 and latitude <= 90.0:
            self.latitude = latitude
        else:
            raise ValueError("Latitude must be between -90.0 and 90.0.")

        if longitude and isinstance(longitude, (int, float)) and longitude >= -180.0 and longitude <= 180.0:
            self.longitude = longitude
        else:
            raise ValueError("Latitude must be between -180.0 and 180.0.")

        self.owner_id = owner_id
        self.reviews = []
        self.amenities = amenities

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
            'amenities': self.amenities,
            'created_at': self.created_at.isoformat() if hasattr(self, 'created_at') else None,
        }
