from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Tile_Store(db.Model, UserMixin):
    __tablename__ = 'tile_store'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    house_id = db.Column(db.Integer, nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)
    
    def to_dict(self):
        return {
            'house_id': self.house_id,
            'data': self.data
        }
