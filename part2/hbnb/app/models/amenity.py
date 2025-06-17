import uuid
from datetime import datetime
from user import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def create_amenity(self):
        pass

    def update_amenity(self):
        pass

    def delete_amenity(self):
        pass

    def list_amenity(self):
        pass