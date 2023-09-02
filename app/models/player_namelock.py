from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Player_Namelock(db.Model, UserMixin):
    __tablename__ = 'player_namelocks'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.String(255), nullable=False)
    namelocked_at = db.Column(db.DateTime, default=datetime.now())
    namelocked_by = db.Column(db.Integer, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'player_id': self.player_id,
            'reason': self.reason,
            'namelocked_at': self.namelocked_at,
            'namelocked_by': self.namelocked_by
        }
