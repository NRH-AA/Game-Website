from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Player_Item(db.Model, UserMixin):
    __tablename__ = 'player_items'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, nullable=False)
    sid = db.Column(db.Integer, nullable=False)
    pid = db.Column(db.Integer, nullable=False, default=0)
    itemtype = db.Column(db.SmallInteger, unsigned=True, nullable=False)
    count = db.Column(db.SmallInteger, nullable=False, default=0)
    attributes = db.Column(db.LargeBinary, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'player_id': self.player_id,
            'sid': self.sid,
            'pid': self.pid,
            'itemtype': self.itemtype,
            'count': self.count,
            'attributes': self.attributes
        }
