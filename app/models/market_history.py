from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Market_History(db.Model, UserMixin):
    __tablename__ = 'market_history'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, unsigned=True, primary_key=True)
    player_id = db.Column(db.Integer, nullable=False)
    sale = db.Column(db.SmallInteger, nullable=False, default=0)
    itemtype = db.Column(db.SmallInteger, unsigned=True, nullable=False)
    amount = db.Column(db.SmallInteger, unsigned=True, nullable=False)
    price = db.Column(db.Integer, unsigned=True, nullable=False, default=0)
    expires_at = db.Column(db.DateTime, unsigned=True, nullable=False)
    inserted = db.Column(db.DateTime, unsigned=True, nullable=False, default=datetime.now())
    state = db.Column(db.SmallInteger, unsigned=True, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'player_id': self.player_id,
            'sale': self.sale,
            'itemtype': self.itemtype,
            'amount': self.amount,
            'price': self.price,
            'expires_at': self.expires_at,
            'inserted': self.inserted,
            'state': self.state
        }
    