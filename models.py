from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from werkzeug.security import generate_password_hash

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    parent = db.relationship('Category', remote_side=[id], backref='subcategories')

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, name, email, role, password):
        self.name = name
        self.email = email
        self.role = role
        self.password = generate_password_hash(password) 

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    location = db.Column(db.String(255))
    tasks = db.relationship('Task', backref='event', lazy=True)

class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    hours_logged = db.Column(db.Float, default=0)
    user = db.relationship('User', backref='volunteers')

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteer.id'))
    hours = db.Column(db.Float)
    description = db.Column(db.Text)
    volunteer = db.relationship('Volunteer', backref='reports')

class TaskAssignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteer.id'))
    status = db.Column(db.String(50), default='Pending')
    volunteer = db.relationship('Volunteer', backref='assignments')
    task = db.relationship('Task', backref='assignments')

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteer.id'))
    attended = db.Column(db.Boolean, default=False)
    event = db.relationship('Event', backref='attendance')
    volunteer = db.relationship('Volunteer', backref='attendance')
