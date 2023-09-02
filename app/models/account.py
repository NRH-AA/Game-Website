from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime
import hashlib


class Account(db.Model, UserMixin):
    __tablename__ = 'accounts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(40), nullable=False)
    secret = db.Column(db.String(16))
    premium_ends_at = db.Column(INTEGER(unsigned=True), nullable=False, default=0)
    email = db.Column(db.String(255), nullable=True)
    creation = db.Column(db.DateTime, default=0)
    
    
    @property
    def hashed_password(self):
        return self.password

    @hashed_password.setter
    def hashed_password(self, password):
        self.password = hashlib.sha1(password.encode('utf-8')).hexdigest()

    def check_password(self, password):
        hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
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
