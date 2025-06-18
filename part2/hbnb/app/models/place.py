import uuid
from datetime import datetime
from app.models.user import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()

        if len(title) <= 100 and isinstance(title, str):
            self.title = title
        else:
            raise ValueError("Title must be a string with 100 characters maximum.")

        if isinstance(description, str):
            self.description = description
        else:
            raise TypeError("Description must be a string.")

        if price > 0 and isinstance(price, float):
            self.price = price
        else:
            raise ValueError("Price must be over 0.")

        if isinstance(latitude, float) and latitude >= -90.0 and latitude <= 90.0:
            self.latitude = latitude
        else:
            raise ValueError("Latitude must be between -90.0 and 90.0.")

        if isinstance(longitude, float) and longitude >= -180.0 and longitude <= 180.0:
            self.longitude = longitude
        else:
            raise ValueError("Latitude must be between -180.0 and 180.0.")

        self.owner = owner
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def create_place(self):
        pass

    def delete_place(self):
        pass

    def list_place(self):
        pass
