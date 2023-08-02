from app.models import db, Account, environment, SCHEMA
from sqlalchemy.sql import text
import hashlib

def seed_accounts():
    account_one = Account(
        name='gigastar', 
        password=hashlib.sha1('password'),
        email='test_email@aol.com'
    )
    
    db.session.add(account_one)
    db.session.commit()


def undo_accounts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.accounts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM accounts"))
        
    db.session.commit()
