from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Account_Viplist(db.Model, UserMixin):
    __tablename__ = 'account_viplist'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    account_id = db.Column(db.Integer)
    player_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.Integer)
    notify = db.Column(db.Integer)
    
    def to_dict(self):
        return {
            'account_id': self.account_id,
            'player_id': self.player_id,
            'description': self.description,
            'icon': self.icon,
            'notify': self.notify
        }
