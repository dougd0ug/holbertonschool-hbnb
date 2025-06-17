import uuid
from datetime import datetime
from user import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    def create_review(self):
        pass

    def update_review(self):
        pass

    def delete_review(self):
        pass

    def list_review(self):
        pass
