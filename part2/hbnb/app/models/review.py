import uuid
from datetime import datetime
from app.models.user import BaseModel
from app.models.place import Place
from app.models.user import User

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        if isinstance(text, str):
            self.text = text
        else:
            raise TypeError("The content of the review must be a string.")

        if isinstance(rating, int) and rating >= 1 and rating >= 5:
            self.rating = rating
        else:
            raise ValueError("The rating must be between 1 and 5")

        place = place_repository.get(place_id)
        if not isinstance(place, Place):
            raise ValueError("Place doesn't exist.")
        self.place = place
        user = user_repository.get(user_id)
        if not isinstance(user, User):
            raise ValueError("User doesn't exist.")
        self.user = user

    def create_review(self):
        pass

    def delete_review(self):
        pass

    def list_review(self):
        pass
