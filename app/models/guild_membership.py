from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Guild_Membership(db.Model, UserMixin):
    __tablename__ = 'guild_membership'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    player_id = db.Column(db.Integer, primary_key=True)
    guild_id = db.Column(db.Integer, nullable=False)
    rank_id = db.Column(db.Integer, nullable=False)
    nick = db.Column(db.Integer, default='New Member')
    
    def to_dict(self):
        return {
            'player_id': self.player_id,
            'guild_id': self.guild_id,
            'rank_id': self.rank_id,
            'nick': self.nick
        }
