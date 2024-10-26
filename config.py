# config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:9876@localhost/task_management'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'abc'  # Change this to a random secret key
    JWT_SECRET_KEY = 'abc'  # Change this to a random secret key
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your_email@gmail.com'
    MAIL_PASSWORD = 'your_email_password'
