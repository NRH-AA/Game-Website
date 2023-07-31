from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime
import hashlib


class Account(db.Model, UserMixin):
    __tablename__ = 'accounts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    