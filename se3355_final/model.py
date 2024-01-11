from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    num_of_comments = db.Column(db.Integer, nullable=False)
    rating= db.Column(db.Float, nullable=False)
    availability = db.Column(db.Integer, default=True)
    member = db.Column(db.Integer,nullable = False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50))
    city = db.Column(db.String(50))