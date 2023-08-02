from flask import Blueprint, jsonify, session, request
from app.models import db, User, Account
from flask_login import current_user, login_user, logout_user, login_required

account_routes = Blueprint('account', __name__)

@account_routes.route('/', methods=['GET'])
def get_accounts():
    accounts = Account.query.all()
    return [account.to_dict() for account in accounts]
