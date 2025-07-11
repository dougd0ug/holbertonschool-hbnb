import uuid
from datetime import datetime
from app.models.user import BaseModel
from app import db
from sqlalchemy.orm import relationship, validates
from sqlalchemy import Column, Integer, String, ForeignKey, Table, true
from app.persistence.base import Base
from app.models.place import place_amenity


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'

    name = db.Column(db.String, nullable=False, unique=True)

    places = relationship("Place", secondary=place_amenity, back_populates="amenities", lazy=True)

    def to_dict(self):
            return {
            "id": self.id,
            "name": self.name,
            }

    @staticmethod
    def part_of_place(self, place):
        self.places.append(place)

    def register_amenity(self):
        pass

    def delete_amenity(self):
        pass

    def update(self, data):
        if 'name' in data:
            if not isinstance('name', str) or not data['name']:
                raise TypeError("Name must be a string.")

        super().update(data)

