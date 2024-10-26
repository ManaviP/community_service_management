# auth.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from models import db, User, Volunteer
from flask_bcrypt import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'msg': 'User already exists'}), 400

    hashed_password = generate_password_hash(data['password']).decode('utf-8')
    new_user = User(name=data['name'], email=data['email'], role=data['role'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'msg': 'User created'}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'msg': 'Bad email or password'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200
