from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade
from flask import request

api = Namespace('admin', description='Admin operations')

user_admin_model = api.model('User_admin', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='password of the user'),
    'is_admin': fields.Boolean(required=True, description='is admin')
})

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})


@api.route('/users/<user_id>')
class AdminUserResource(Resource):
    @api.doc(security='Bearer Auth')
    @api.expect(user_admin_model, validate=True)
    @api.response(200, 'User updated successfully')
    @api.response(400, 'Invalid data or duplicate email')
    @api.response(404, 'User not found')
    @api.response(403, 'Admin privileges required')
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt_identity()
        
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        data = request.get_json()
        email = data.get('email')

        if email:
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email is already in use'}, 400

        user = facade.update_user(user_id, data)
        if not user:
            return {"error": "User not found"}, 404
        return user.to_dict(), 200

    @api.doc(security='Bearer Auth')
    @api.response(200, 'User deleted successfully')
    @api.response(404, 'User not found')
    @api.response(403, 'Admin privileges required')
    @jwt_required()
    def delete(self, user_id):
        """Delete any user (admin only)"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        facade.delete_user(user_id)
        return {"message": "User deleted successfully"}, 200


@api.route('/')
class AdminUserList(Resource):
    @api.doc(security='Bearer Auth')
    @api.response(200, 'List of users retrieved successfully')
    @api.response(403, 'Admin privileges required')
    @jwt_required()
    def get(self):
        """List all users (admin only)"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        users = facade.get_all_users()
        return [u.to_dict() for u in users], 200

    @api.doc(security='Bearer Auth')
    @api.expect(user_admin_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(403, 'Admin privileges required')
    @jwt_required()
    def post(self):
        """Create a user (admin only, can set is_admin)"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        data = request.get_json()
        if facade.get_user_by_email(data.get("email")):
            return {"error": "Email already registered"}, 400
        user = facade.create_user(data)
        return user.to_dict(), 201
