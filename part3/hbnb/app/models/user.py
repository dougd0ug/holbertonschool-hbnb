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
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        
        if not first_name or not isinstance(first_name, str) or len(first_name) > 50:
            raise ValueError("First name must be a non-empty string with 50 characters maximum.")
        self.first_name = first_name

        if not last_name or not isinstance(last_name, str) or len(last_name) > 50:
            raise ValueError("Last name must be a non-empty string with 50 characters maximum.")
        self.last_name = last_name

        if not email or not self.valid_email(email):
            raise ValueError("Email address is not valid.")
        self.email = email

        if not isinstance(is_admin, bool):
            raise TypeError("is_admin must be True or False.")
        self.is_admin = is_admin
        self.places = []
        self.password = password

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

    def to_dict(self):
        return {
        "id": self.id,
        "first_name": self.first_name,
        "last_name": self.last_name,
        "email": self.email
        }

    def update(self, data):
        if 'first_name' in data:
            if not isinstance(data['first_name'], str) or len(data['first_name']) > 50 or not data['first_name']:
                raise ValueError("First name must be a non-empty string with 50 characters max")

        if 'last_name' in data:
            if not isinstance(data['last_name'], str) or len(data['last_name']) > 50 or not data['last_name']:
                raise ValueError("Last name must be a non-empty string with 50 characters max")

        if 'email' in data:
            if not self.valid_email(data['email']) or not data['email']:
                raise ValueError("Invalid email format")

        if 'is_admin' in data:
            if not isinstance(data['is_admin'], bool):
                raise TypeError("is_admin must be a boolean")

        super().update(data)

    def hash_password(self, password):
        """Hashes the password before storing it."""
        from app import bcrypt
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        from app import bcrypt
        return bcrypt.check_password_hash(self.password, password)
