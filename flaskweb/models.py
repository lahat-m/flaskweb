from datetime import datetime
from flaskweb import db, login_manager
from flask_login import UserMixin

# This function is used by Flask-Login to load a user from the user_id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# User class represents a user in the application and inherits from db.Model and UserMixin
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)  # Column for storing username
    email = db.Column(db.String(120), unique=True, nullable=False)  # Column for storing email
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')  # Column for storing profile image file name
    password = db.Column(db.String(60), nullable=False)  # Column for storing hashed password
    posts = db.relationship('Post', backref='author', lazy=True)  # Relationship with Post model, allows accessing posts by a user

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# Post class represents a post in the application and inherits from db.Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # Column for storing post title
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Column for storing post creation date
    content = db.Column(db.Text, nullable=False)  # Column for storing post content
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key column referencing user who created the post

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
