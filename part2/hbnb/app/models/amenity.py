import uuid
from datetime import datetime
from user import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name must be a string.")

    def create_amenity(self):
        pass

    def delete_amenity(self):
        pass

    def list_amenity(self):
        pass