from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Player_Spell(db.Model, UserMixin):
    __tablename__ = 'player_spells'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'player_id': self.player_id,
            'name': self.name
        }
