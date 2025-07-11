import uuid
from datetime import datetime
from app.models.user import BaseModel
from app import db
from sqlalchemy.orm import relationship, validates
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from app.persistence.base import Base
from app.models.place import place_amenity_association


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    places = relationship("Place", secondary=place_amenity_association, back_populates="amenities")

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

