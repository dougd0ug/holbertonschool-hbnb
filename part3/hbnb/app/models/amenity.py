import uuid
from datetime import datetime
from app.models.user import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        if name and isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name must be a string.")

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
