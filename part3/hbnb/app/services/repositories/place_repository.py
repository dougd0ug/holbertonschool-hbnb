from app.models.place import Place
from app import db
from app.persistence.repository import SQLAlchemyRepository

class PlaceRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Place)

    def get_amenity_by_name(self, name):
        return self.model.query.filter_by(name=name).first()
