from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Account_Ban(db.Model, UserMixin):
    __tablename__ = 'account_bans'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    account_id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.Text, nullable=True)
    banned_at = db.Column(db.DateTime, default=datetime.now())
    expires_at = db.Column(db.DateTime, nullable=False)
    banned_by = db.Column(db.String(50), nullable=False)
    
    def to_dict(self):
        return {
            'account_id': self.account_id,
            'reason': self.reason,
            'banned_at': self.banned_at,
            'expires_at': self.expires_at,
            'banned_by': self.banned_by
        }
