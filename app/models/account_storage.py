from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.dialects.mysql import INTEGER
from flask_login import UserMixin

class Account_Storage(db.Model, UserMixin):
    __tablename__ = 'account_storage'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, nullable=False, default=0)
    key = db.Column(INTEGER(unsigned=True), nullable=False, default=0)
    value = db.Column(db.Integer, nullable=False, default=0)
    
    def to_dict(self):
        return {
            'id': self.id,
            'account_id': self.account_id,
            'key': self.key,
            'value': self.value
        }
