from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Guildwar_kill(db.Model, UserMixin):
    __tablename__ = 'guildwar_kills'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    killer = db.Column(db.Integer, nullable=False)
    target = db.Column(db.Integer, nullable=False)
    killerguild = db.Column(db.Integer, nullable=False)
    targetguild = db.Column(db.Integer, nullable=False)
    warid = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, default=datetime.now())
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'killer': self.killer,
            'target': self.target,
            'killerguild': self.killerguild,
            'targetguild': self.targetguild,
            'warid': self.warid,
            'time': self.time
        }
