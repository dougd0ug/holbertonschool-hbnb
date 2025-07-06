from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade

api = Namespace('admin', description='Admin operations')

user_admin_model = api.model('User_admin', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='password of the user'),
    'is_admin': fields.Boolean(required=True, descrition='is admin')
})

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})
