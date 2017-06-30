from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database/app.db')
print('sqlite:///' + os.path.join(basedir, 'database/app.db'))

db=SQLAlchemy(app)

class Points(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lon = db.Column(db.Float, unique=False)
    lat = db.Column(db.Float, unique=False)
    name = db.Column(db.String(128), unique=False)
    comment = db.Column(db.String(256), unique=False)
    idcat = db.Column(db.Integer, unique=False)
    time_ago = db.Column(db.String(50), unique=False)
    is_camera = db.Column(db.Boolean, unique=False)

    def __init__(self, lat, lon, name, comment, idcat, time_ago, is_camera):
        self.lat = lat
        self.lon = lon
        self.name = name
        self.comment = comment
        self.idcat = idcat
        self.time_ago = time_ago
        self.is_camera = is_camera


    def __repr__(self):
        return "%d, %f, %f, %s, %s, %d, %s\n" %(self.id, self.lat, self.lon, self.name, self.comment, self.idcat, self.time_ago)

from app import views