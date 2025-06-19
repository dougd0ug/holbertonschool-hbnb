import uuid
from datetime import datetime
import re


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Update the updated_at timestamp

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()

        if len(first_name) <= 50 and isinstance(first_name, str):
            self.first_name = first_name
        else:
            raise ValueError("Your first name must be a string and have 50 characters maximum.")

        if len(last_name) <= 50 and isinstance(last_name, str):
            self.last_name = last_name
        else:
            raise ValueError("Your last name must be a string and have 50 characters maximum.")

        if self.valid_email(email):
            self.email = email
        else:
            raise ValueError("Mail adress is not valid.")

        if isinstance(is_admin, bool):
            self.is_admin = is_admin
        else:
            raise TypeError("You must be either a user or an admin.")
        self.places = []

        def to_dict(self):
            return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
            }

    @staticmethod
    def valid_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    def owns_place(self, place):
        self.places.append(place)

    def register_user(self):
        pass

    def delete_user(self):
        pass
