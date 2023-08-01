from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Player_Namelock(db.Model, UserMixin):
    __tablename__ = 'player_namelocks'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    player_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    
    def to_dict(self):
        return {
            'player_id': self.player_id,
            'name': self.name
        }
