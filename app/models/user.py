from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime
import hashlib

default_image = 'https://www.computerhope.com/jargon/g/guest-user.png'

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    profile_picture = db.Column(db.Text, default=default_image)
    active = db.Column(db.Boolean, default=True)
    theme = db.Column(db.String(255), default='light')
    createdAt = db.Column(db.DateTime, default=datetime.now())
    updatedAt = db.Column(db.DateTime, default=datetime.now())


    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = hashlib.sha256(password)

    def check_password(self, password):
        hashed_password = hashlib.sha256(password)
        return self.password == hashed_password

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'profile_picture': self.profile_picture,
            'active': self.active,
            'theme': self.theme,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
