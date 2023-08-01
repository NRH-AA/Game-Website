from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Town(db.Model, UserMixin):
    __tablename__ = 'towns'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    posx = db.Column(db.Integer, nullable=False, default=0)
    posy = db.Column(db.Integer, nullable=False, default=0)
    posz = db.Column(db.Integer, nullable=False, default=0)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'posx': self.posx,
            'posy': self.posy,
            'posz': self.posz
        }
