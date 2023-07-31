from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime
import hashlib


class Account(db.Model, UserMixin):
    __tablename__ = 'accounts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    secret = db.Column(db.Integer, nullable=True)
    premium_ends_at = db.Column(db.Integer, default=0)
    email = db.Column(db.String(70), nullable=True)
    creation = db.Column(db.DateTime, default=datetime.now())
    
    
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password):
        self.password = hashlib.sha1(password)

    def check_password(self, password):
        hashed_password = hashlib.sha1(password)
        return self.password == hashed_password

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'secret': self.secret,
            'premium_ends_at': self.premium_ends_at,
            'email': self.email,
            'creation': self.creation
        }
