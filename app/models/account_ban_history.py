from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Account_Ban_History(db.Model, UserMixin):
    __tablename__ = 'account_ban_history'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(255), nullable=False)
    banned_at = db.Column(db.DateTime, default=datetime.now())
    expires_at = db.Column(db.DateTime, nullable=False)
    banned_by = db.Column(db.Integer, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'account_id': self.account_id,
            'reason': self.reason,
            'banned_at': self.banned_at,
            'expires_at': self.expires_at,
            'banned_by': self.banned_by
        }
