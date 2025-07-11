import uuid
from datetime import datetime
import re
from app import bcrypt, db
from app.models.baseclasse import BaseModel
from sqlalchemy.orm import relationship, validates
from sqlalchemy import Column, Integer, String, ForeignKey
from app.persistence.base import Base


class User(BaseModel, Base):
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=True)

    places = relationship("Place", back_populates="owner", lazy=True)

    reviews = relationship("Review", back_populates="user", lazy=True)

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

    @validates("first_name")
    def validate_first_name(self, key, first_name):
        if not first_name or len(first_name) > 50:
            raise ValueError("First name must be a non-empty string with 50 characters max.")
        else:
            return first_name
    
    @validates("last_name")
    def validate_last_name(self, key, last_name):
        if not last_name or len(last_name) > 50:
            raise ValueError("Last name must be a non-empty string with 50 characters max.")
        else:
            return last_name

    @validates("email")
    def validate_email(self, key, email):
        if not self.valid_email(email):
            raise ValueError("Invalid email format.")
        else:
            return email

    @staticmethod
    def valid_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None
