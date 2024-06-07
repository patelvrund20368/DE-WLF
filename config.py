import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://admin:admin12345@database-1.czc86ksg6zj0.eu-north-1.rds.amazonaws.com:3306/wildlife_rescue'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
