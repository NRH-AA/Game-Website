from flask import Blueprint, jsonify, session, request
from app.models import db, User, Account
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime
import hashlib

account_routes = Blueprint('account', __name__)

@account_routes.route('/', methods=['GET'])
def get_accounts():
    accounts = Account.query.all()
    return {'accounts': [account.to_dict() for account in accounts]}


@account_routes.route('/', methods=['POST'])
def create_account():
    data = request.get_json()
    name = data['name']
    password = data['password']
    confirm_password = data['confirmPassword']
    email = data['email']
    
    if not password == confirm_password:
        return {'error': 'Passwords must match'}
    
    check_account_id = Account.query.where(
        Account.name.ilike(name)
    )
    
    if check_account_id.count() > 0:
        return {'error': 'Invalid account name.'}

    check_email = Account.query.where(
        Account.email.ilike(email)
    )
    
    if check_email.count() > 0:
        return {'error': 'Email in use.'}
    
    password = hashlib.sha1(password.encode('utf-8')).hexdigest()
    
    new_account = Account(
        name=name,
        password=password,
        email=email
    )
    
    db.session.add(new_account)
    db.session.commit()
    return {'success': 'Account has been created!'}
    
    