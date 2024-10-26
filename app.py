from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from config import Config
from models import db, User, Event, Volunteer, Task, Report, Attendance
from auth import auth

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
mail = Mail(app)

@app.before_first_request
def create_tables():
    db.create_all()

# User authentication routes
app.register_blueprint(auth)

# Notification function
def send_notification(email, subject, body):
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.body = body
    mail.send(msg)

# Event creation with notification
@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    new_event = Event(
        name=data['name'], 
        description=data['description'], 
        date=data['date'], 
        location=data['location']
    )
    db.session.add(new_event)
    db.session.commit()

    # Notify all volunteers
    volunteers = Volunteer.query.all()
    for volunteer in volunteers:
        send_notification(volunteer.user.email, "New Event Created", f"Event '{new_event.name}' has been created.")

    return jsonify({'id': new_event.id}), 201

# Get events
@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{
        'id': e.id, 
        'name': e.name, 
        'description': e.description, 
        'date': e.date.isoformat(), 
        'location': e.location
    } for e in events])

# Attendance tracking
@app.route('/attendance', methods=['POST'])
def log_attendance():
    data = request.get_json()
    attendance = Attendance(
        event_id=data['event_id'], 
        volunteer_id=data['volunteer_id'], 
        attended=data['attended']
    )
    db.session.add(attendance)
    db.session.commit()
    return jsonify({'msg': 'Attendance logged'}), 201

# Categories
@app.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    new_category = Category(
        name=data['name'], 
        parent_id=data.get('parent_id')
    )
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'id': new_category.id}), 201

@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{
        'id': c.id, 
        'name': c.name, 
        'parent_id': c.parent_id 
    } for c in categories])

# Users
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        name=data['name'], 
        email=data['email'], 
        role=data['role']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': u.id, 
        'name': u.name, 
        'email': u.email, 
        'role': u.role 
    } for u in users])

# Volunteers
@app.route('/volunteers', methods=['POST'])
def register_volunteer():
    data = request.get_json()
    volunteer = Volunteer(user_id=data['user_id'])
    db.session.add(volunteer)
    db.session.commit()
    return jsonify({'id': volunteer.id}), 201

@app.route('/volunteers', methods=['GET'])
def get_volunteers():
    volunteers = Volunteer.query.all()
    return jsonify([{
        'id': v.id, 
        'user_id': v.user_id, 
        'hours_logged': v.hours_logged 
    } for v in volunteers])

# Tasks
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(
        name=data['name'], 
        description=data['description'], 
        event_id=data['event_id']
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'id': new_task.id}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{
        'id': t.id, 
        'name': t.name, 
        'description': t.description, 
        'event_id': t.event_id 
    } for t in tasks])

# Reports
@app.route('/reports', methods=['POST'])
def create_report():
    data = request.get_json()
    new_report = Report(
        volunteer_id=data['volunteer_id'], 
        hours=data['hours'], 
        description=data['description']
    )
    db.session.add(new_report)
    db.session.commit()
    return jsonify({'id': new_report.id}), 201

@app.route('/reports', methods=['GET'])
def get_reports():
    reports = Report.query.all()
    return jsonify([{
        'id': r.id, 
        'volunteer_id': r.volunteer_id, 
        'hours': r.hours, 
        'description': r.description 
    } for r in reports])

if __name__ == '__main__':
    app.run(debug=True)
