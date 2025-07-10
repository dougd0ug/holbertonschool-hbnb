import uuid
from datetime import datetime
import re
from app import bcrypt, db
from app.models.baseclasse import BaseModel

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<User {self.email}>"

    def hash_password(self, plain_password):
        self.password = bcrypt.generate_password_hash(plain_password).decode('utf-8')

    def verify_password(self, plain_password):
        return bcrypt.check_password_hash(self.password, plain_password)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin
        }

    def validate(self):
        if not self.first_name or len(self.first_name) > 50:
            raise ValueError("First name must be a non-empty string with 50 characters max.")
        if not self.last_name or len(self.last_name) > 50:
            raise ValueError("Last name must be a non-empty string with 50 characters max.")
        if not self.valid_email(self.email):
            raise ValueError("Invalid email format.")
        if not isinstance(self.is_admin, bool):
            raise TypeError("is_admin must be a boolean.")

    @staticmethod
    def valid_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None
