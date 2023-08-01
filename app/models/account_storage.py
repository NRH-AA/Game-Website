from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Account_Storage(db.Model, UserMixin):
    __tablename__ = 'account_storage'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    account_id = db.Column(db.Integer, nullable=False, default=0)
    key = db.Column(db.Integer, unsigned=True, nullable=False, default=0)
    value = db.Column(db.Integer, nullable=False, default=0)
    
    def to_dict(self):
        return {
            'account_id': self.account_id,
            'key': self.key,
            'value': self.value
        }
