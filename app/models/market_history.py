from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Market_History(db.Model, UserMixin):
    __tablename__ = 'market_history'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, nullable=False)
    sale = db.Column(db.Integer, nullable=False)
    itemtype = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    expires_at = db.Column(db.DateTime, default=datetime.now())
    inserted = db.Column(db.Integer, nullable=False)
    state = db.Column(db.Integer, nullable=False)
    
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
    