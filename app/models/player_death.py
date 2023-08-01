from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Player_Death(db.Model, UserMixin):
    __tablename__ = 'player_deaths'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    player_id = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, unsinged=True, nullable=False, default=datetime.now())
    level = db.Column(db.Integer, nullable=False, default=1)
    killed_by = db.Column(db.String(255), nullable=False)
    is_player = db.Column(db.SmallInteger, nullable=False, default=1)
    mostdamage_by = db.Column(db.String(100), nullable=False)
    mostdamage_is_player = db.Column(db.SmallInteger, nullable=False, default=0)
    unjustified = db.Column(db.SmallInteger, nullable=False, default=0)
    mostdamage_unjustified = db.Column(db.SmallInteger, nullable=False, default=0)
    
    def to_dict(self):
        return {
            'player_id': self.player_id,
            'time': self.time,
            'level': self.level,
            'killed_by': self.killed_by,
            'is_player': self.is_player,
            'mostdamage_by': self.mostdamage_by,
            'mostdamage_is_player': self.mostdamage_is_player,
            'unjustified': self.unjustified,
            'mostdamage_unjustified': self.mostdamage_unjustified
        }
