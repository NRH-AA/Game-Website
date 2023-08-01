from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Players_Online(db.Model, UserMixin):
    __tablename__ = 'players_online'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    player_id = db.Column(db.Integer, unique=True, nullable=False)
    
    def to_dict(self):
        return {
            'player_id': self.player_id
        }
    