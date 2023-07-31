from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Guild_Rank(db.Model, UserMixin):
    __tablename__ = 'guild_ranks'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    guild_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(50), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'guild_id': self.guild_id,
            'name': self.name,
            'level': self.level
        }
