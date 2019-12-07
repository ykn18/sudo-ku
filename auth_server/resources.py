from flask_restful import Resource, reqparse
from models import UserModel
from lib_token import create_token

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)

class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message': 'User {} already exists'.format(data['username'])}
        
        new_user = UserModel(
            username = data['username'],
            password = UserModel.generate_hash(data['password'])
        )
        
        try:
            new_user.save_to_db()
            return {'token' : create_token(data['username'])}, 201
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])
        if current_user == None:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}, 400
        
        if UserModel.verify_hash(data['password'], current_user.password):
            return {'token' : create_token(data['username'])}, 200
        else:
            return {'message': 'Wrong credentials'}, 400
      