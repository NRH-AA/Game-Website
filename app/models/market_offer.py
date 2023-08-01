from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Market_Offer(db.Model, UserMixin):
    __tablename__ = 'market_offers'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, nullable=False)
    sale = db.Column(db.Integer, nullable=False)
    itemtype = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    anonymous = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'player_id': self.player_id,
            'sale': self.sale,
            'itemtype': self.itemtype,
            'amount': self.amount,
            'created': self.created,
            'anonymous': self.anonymous,
            'price': self.price
        }
