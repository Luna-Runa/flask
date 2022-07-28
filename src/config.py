import os

from flask_sqlalchemy import SQLAlchemy

user = os.getenv('PG_USER')
password = os.getenv('PG_PASSWORD')
host = os.getenv('PG_HOST')
database = os.getenv('PG_DB')
port = os.getenv('PG_PORT')

SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

FLASK_APP = os.getenv('FLASK_APP')
FLASK_ENV = os.getenv('FLASK_ENV')
FLASK_DEBUG = os.getenv('FLASK_DEBUG')
FLASK_PORT = os.getenv('FLASK_PORT')
SECRET_KEY = os.getenv('SECRET_KEY')