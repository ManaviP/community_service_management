# utils.py

from models import Volunteer

def log_hours(volunteer_id, hours):
    volunteer = Volunteer.query.get(volunteer_id)
    volunteer.hours_logged += hours
    db.session.commit()
