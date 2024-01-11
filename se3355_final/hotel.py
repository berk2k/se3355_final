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