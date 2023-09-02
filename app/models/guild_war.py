from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Guild_War(db.Model, UserMixin):
    __tablename__ = 'guild_wars'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    guild1 = db.Column(db.Integer, nullable=False, default=0)
    guild2 = db.Column(db.Integer, nullable=False, default=0)
    name1 = db.Column(db.String(255), nullable=False)
    name2 = db.Column(db.String(255), nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)
    started = db.Column(db.DateTime, default=datetime.now())
    ended = db.Column(db.DateTime, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'guild1': self.guild1,
            'guild2': self.guild2,
            'name1': self.name1,
            'name2': self.name2,
            'status': self.status,
            'started': self.started,
            'ended': self.ended
        }
