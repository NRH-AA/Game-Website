from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.dialects.mysql import SMALLINT, INTEGER
from flask_login import UserMixin
from datetime import datetime

class Market_Offer(db.Model, UserMixin):
    __tablename__ = 'market_offers'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    player_id = db.Column(db.Integer, nullable=False)
    sale = db.Column(db.SmallInteger, nullable=False, default=0)
    itemtype = db.Column(SMALLINT(unsigned=True), nullable=False)
    amount = db.Column(SMALLINT(unsigned=True), nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    anonymous = db.Column(db.SmallInteger, nullable=False, default=0)
    price = db.Column(INTEGER(unsigned=True), nullable=False, default=0)
    
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
