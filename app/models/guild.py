from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin

class Guild(db.Model, UserMixin):
    __tablename__ = 'guilds'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ownerid = db.Column(db.Integer, nullable=False)
    creationdata = db.Column(db.Text)
    motd = db.Column(db.Text)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ownerid': self.ownerid,
            'creationdata': self.creationdata,
            'motd': self.motd
        }
