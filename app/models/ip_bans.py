from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Ip_Bans(db.Model, UserMixin):
    __tablename__ = 'ip_bans'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.String(255), nullable=False)
    banned_at = db.Column(db.DateTime, default=datetime.now())
    expires_at = db.Column(db.DateTime, nullable=False)
    banned_by = db.Column(db.Integer, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'reason': self.reason,
            'banned_at': self.banned_at,
            'expires_at': self.expires_at,
            'banned_by': self.banned_by
        }
