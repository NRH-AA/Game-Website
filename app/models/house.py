from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class House(db.Model, UserMixin):
    __tablename__ = 'houses'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, nullable=False)
    paid = db.Column(db.Integer, unsigned=True, nullable=False, default=0)
    warnings = db.Column(db.Integer, nullable=False, default=0)
    name = db.Column(db.String(255), nullable=False)
    rent = db.Column(db.Integer, nullable=False, default=0)
    town_id = db.Column(db.Integer, nullable=False, default=0)
    bid = db.Column(db.Integer, nullable=False, deafult=0)
    bid_end = db.Column(db.Integer, nullable=False, deafult=0)
    last_bid = db.Column(db.Integer, nullable=False, deafult=0)
    highest_bidder = db.Column(db.Integer, nullable=False, deafult=0)
    size = db.Column(db.Integer, nullable=False, deafult=0)
    beds = db.Column(db.Integer, nullable=False, deafult=0)
    
    def to_dict(self):
        return {
            'id': self.id,
            'owner': self.owner,
            'paid': self.paid,
            'warnings': self.warnings,
            'name': self.name,
            'rent': self.rent,
            'town_id': self.town_id,
            'bid': self.bid,
            'bid_end': self.bid_end,
            'last_bid': self.last_bid,
            'highest_bidder': self.highest_bidder,
            'size': self.size,
            'beds': self.beds
        }
