classDiagram
class PresentationLayer {
    <<Interface>>
    +Reservation
    +Post an annonce
    +Post a review
    +Send messages
    +Create an account
    +Be an administrator
}
class BusinessLogicLayer {
    +User Entity
    +Place Entity
    +Review Entity
    +Amenity Entity
}
class PersistenceLayer {
    +Database
}
PresentationLayer --> BusinessLogicLayer : Facade Pattern
BusinessLogicLayer --> PersistenceLayer : Database Operations