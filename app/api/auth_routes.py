from flask import Blueprint, jsonify, session, request
from app.models import User, db
from flask_login import current_user, login_user, logout_user, login_required

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/')
def authenticate():
    if current_user.is_authenticated:
        return current_user.to_dict_all()
    return {'errors': ['Unauthorized']}


@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    account_id = data['accountid']
    email = data['email']
    password = data['password']
    
    user = False
    if email:
        user = User.query.filter(User.email == email).first()
        
    if account_id:
        user = User.query.filter(User.account_id == account_id).first()
        
    if not user:
         return {'email': 'Invalid credentials provided'}, 401
        
    if not user.check_password(password):
        return {'password': ['Invalid password provided']}, 401
        
    login_user(user)
    return user.to_dict()


@auth_routes.route('/logout')
def logout():
    """
    Logs a user out
    Returns a dictionary {'message': 'User logged out'}
    """
    logout_user()
    return {'message': 'User logged out'}


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Signs a user up. 
    Expecting a dictionary with {email, username, password, confirmPassword}
    """
    data = request.get_json()
    email = data['email']
    username = data['username']
    password = data['password']
    confirm_password = data['confirmPassword']
    
    errors = {}
        
    if not email or len(email) < 4:
        errors['email'] = 'Email must be 4 characters or more'
        
    if not username or len(username) < 4:
        errors['username'] = 'Username must be 4 characters or more'
        
    if not password or len(password) < 4:
        errors['password'] = 'Password must be 4 characters or more'
        
    if not confirm_password or confirm_password != password:
        errors['confirm_password'] = 'Confirm password does not match'

    if len(errors) > 0:
        return {'errors': errors}, 400
    
    check_user = User.query.filter(User.email == email).first()
    
    if check_user:
        errors['emailTaken'] = 'Email is already in use'
        return {'errors': errors}, 400

    user = User(
        username = username,
        email = email,
        password = password
    )
    db.session.add(user)
    db.session.commit()
    
    login_user(user)
    return user.to_dict()


@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': ['Unauthorized']}, 401
