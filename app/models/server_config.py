from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Server_Config(db.Model, UserMixin):
    __tablename__ = 'server_config'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    config = db.Column(db.String(50), nullable=False, default=0)
    value = db.Column(db.String(255), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'config': self.config,
            'value': self.value
        }
    