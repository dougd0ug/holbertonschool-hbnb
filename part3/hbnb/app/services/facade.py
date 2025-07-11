from app.persistence.repository import InMemoryRepository
from app.persistence.repository import SQLAlchemyRepository
from app.services.repositories.user_repository import UserRepository
from app.services.repositories.amenity_repository import AmenityRepository
from app.services.repositories.review_repository import ReviewRepository
from app.services.repositories.place_repository import PlaceRepository
from app.models.user import User, BaseModel
from app.models.amenity import Amenity
from app.models.review import Review
from app.models.place import Place
from app import db


class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.place_repo = PlaceRepository()
        self.amenity_repo = AmenityRepository()
        self.review_repo = ReviewRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)
    
    def get_all_users(self):
        return self.user_repo.get_all()
    
    def update_user(self, user_id, update_data):
        return self.update(user_id, update_data)

    def update(self, user_id, update_data):
        user = self.get_user(user_id)
        if not user:
            return None

        if "email" in update_data:
            new_email = update_data["email"]
            existing_user = self.user_repo.get_user_by_email(new_email)
            if existing_user and existing_user.id != user.id:
                raise ValueError("Email already registered to another user")

        for key, value in update_data.items():
            if hasattr(user, key):
                if key == "password":
                    user.hash_password(value)
                else:
                    setattr(user, key, value)
    
    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def create_place(self, place_data):
        price = place_data.get('price')
        latitude = place_data.get('latitude')
        longitude = place_data.get('longitude')

        if price is None or price < 0:
            raise ValueError("Price must be a non-negative float.")
        if latitude is None or not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90.")
        if longitude is None or not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180.")

        owner_id = place_data.get('owner_id')
        owner = self.user_repo.get(owner_id)
        if not owner:
            raise ValueError("The specified owner does not exist.")

        amenities_ids = place_data.get('amenities', [])
        amenities = []
        for amenity_id in amenities_ids:
            amenity = self.amenity_repo.get(amenity_id)
            if not amenity:
                raise ValueError(f"Amenity not found: {amenity_id}")
            amenities.append(amenity)

        place = Place(
            title=place_data['title'],
            price=price,
            latitude=latitude,
            longitude=longitude,
            owner=owner,
            description=place_data.get('description', "")
        )
        place.amenities = amenities
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        place = self.place_repository.get(place_id)
        if not place:
            raise ValueError("Place not found.")
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        if 'price' in place_data and place_data['price'] < 0:
            raise ValueError("Price must be a non-negative float.")
        if 'latitude' in place_data and not (-90 <= place_data['latitude'] <= 90):
            raise ValueError("Latitude must be between -90 and 90.")
        if 'longitude' in place_data and not (-180 <= place_data['longitude'] <= 180):
            raise ValueError("Longitude must be between -180 and 180.")

        if 'owner_id' in place_data:
            owner = self.user_repo.get(place_data['owner_id'])
            if not owner:
                raise ValueError("The specified owner does not exist.")
            place_data['owner'] = owner
            del place_data['owner_id']

        if 'amenities' in place_data:
            amenity_ids = place_data['amenities']
            amenities = []
            for amenity_id in amenity_ids:
                amenity = self.amenity_repo.get(amenity_id)
                if not amenity:
                    raise ValueError(f"Amenity not found: {amenity_id}")
                amenities.append(amenity)
            place_data['amenities'] = amenities

        return self.place_repo.update(place_id, place_data)

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity_by_name(self, amenity_name):
        return self.amenity_repo.get(amenity_name)
    
    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
    
        amenity.update(amenity_data)
        return amenity


    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        all_reviews = self.review_repo.get_all()
        return [review for review in all_reviews if review.place_id == place_id]

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if not review:
            return None

        review.update(review_data)
        return review

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        self.review_repo.delete(review_id)
        return review

    def delete_user(self, user_id):
        user = self.user_repo.get(user_id)
        self.user_repo.delete(user_id)
        return user
