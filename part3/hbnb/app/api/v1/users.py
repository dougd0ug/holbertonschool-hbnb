from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade
from app.models.user import User

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user')
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    @api.response(404, 'User not found')
    @api.response(403, 'Invalid password')

    def post(self):
        """Register a new user"""
        user_data = api.payload

        existing_user = facade.get_user_by_email(user_data['email'])

        if existing_user:
            return {'error': 'Email already registered'}, 400

        try:
            # Hash the password before storing
            user_data['password'] = hash_password(user_data['password'])
            new_user = facade.create_user(user_data)
        except Exception as e:
            return {'error': str(e)}, 400

        return {'id': new_user.id, 
                'first_name': new_user.first_name, 
                'last_name': new_user.last_name, 
                'email': new_user.email}, 201


    def get_by_email(self, user_email):
        """Get user details by email"""
        user = facade.get_user_by_email(user_email)
        user_data = api.payload

        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email}, 200

    def get(self):
        """Get all list users"""
        users = facade.get_all_users()
        return [user.to_dict() for user in users], 200

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)

        if not user:
            return {'error': 'User not found'}, 404

        return {'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email}, 200

    @api.expect(user_model, validate=True)
    @api.response(200, 'User successfully updated')
    @api.response(404, 'User doesnt exist')
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
        """Updates user details"""
        user_data = api.payload

        try:
            updated_user = facade.update_user(user_id, user_data)
        except Exception as e:
            return {'error': str(e)}, 400

        if not updated_user:
            return {'error': 'User not found'}, 404

        return updated_user.to_dict(), 200
