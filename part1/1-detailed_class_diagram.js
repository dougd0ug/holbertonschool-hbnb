classDiagram
direction TB
    class USER {
	    -id UUID
	    -first_name : string
	    -last_name : string
	    -email : string
	    -password : string
	    -admin : boolean
	    -created_at : date
	    -updated_at : date
	    +register_user()
	    +update_user()
	    +delete_user()
    }

    class PLACE {
	    -id UUID
	    +title : string
	    +description : string
	    +price : float
	    +latitude : float
	    +longitude : float
	    +create_place()
	    +update_place()
	    +delete_place()
	    +list_place()
    }

    class AMENITY {
	    -id UUID
	    +name : string
	    +description : string
	    +create_amenity()
	    +update_amenity()
	    +delete_amenity()
	    +list_amenity()
    }

    class REVIEW {
	    -id UUID
	    +user : string
	    +place : string
	    +rating : int
	    +comment : string
	    +create_review()
	    +update_review()
	    delete_review()
	    list_review()
    }

    USER --|> PLACE : owns
    PLACE o-- AMENITY : part of
    PLACE --> REVIEW : associate

