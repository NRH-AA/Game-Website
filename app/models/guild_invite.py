from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Guild_Invite(db.Model, UserMixin):
    __tablename__ = 'guild_invites'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    player_id = db.Column(db.Integer, nullable=False, default=0)
    guild_id = db.Column(db.Integer, nullable=False, default=0)
    
    def to_dict(self):
        return {
            'player_id': self.player_id,
            'guild_id': self.guild_id
        }
