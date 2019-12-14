from flask import Flask, jsonify, request, json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bcrypt import Bcrypt
from datetime import datetime
from lib_token import create_token

app = Flask(__name__)
app.config['MONGODB_NAME'] = 'authentication_db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/authentication_db'
app.config['SECRET_KEY'] = 'mysecretkey'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)

@app.route('/register', methods=['POST'])
def register():
    users = mongo.db.users
    data = request.get_json()
    username = data['username']

    exsists = users.find_one({'username' : username})
    if(exsists):
        response = {"message" : "Username {} already exsits".format(username)}
        return jsonify(response), 409 #resource already exsists
    
    password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    created = datetime.utcnow()

    user_id = users.insert({
        'username' : username,
        'password' : password,
        'role' : 'USER',
        'created' : created
    })
    token = create_token(app.config['SECRET_KEY'], username) 
    response = {'token' : token}
    return jsonify(response), 201
    
@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = users.find_one({'username' : username})
    if(user):
        if bcrypt.check_password_hash(user["password"], password):
            token = create_token(app.config['SECRET_KEY'], user["username"]) 
            response = {'token' : token}
            return jsonify(response), 200
        else:
            response = {'message' : 'Wrong credentials'}
            return jsonify(response), 400
    else:
        response = {'message': 'User {} doesn\'t exist'.format(username)}
        return jsonify(response), 400
