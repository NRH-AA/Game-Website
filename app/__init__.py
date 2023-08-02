from os import environ

from flask import Flask, render_template, request, session, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager

from .models import db, User

from .api.user_routes import user_routes
from .api.auth_routes import auth_routes
from .api.player_routes import player_routes

from .seeds import seed_commands

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')


# Set up login manager
login = LoginManager(app)
login.login_view = 'auth.unauthorized'
@login.user_loader
def load_user(id):
    pass


# Tell flask about our seed commands
app.cli.add_command(seed_commands)

######## DATABASE INFORMATION ###########
DB_USER = environ.get('DB_USER')
DB_PASSWORD = environ.get('DB_PASSWORD')
DB_HOST = environ.get('DB_HOST')
DB_NAME = environ.get('DB_NAME')


# Update app config
app.config.update(
    SECRET_KEY = environ.get('SECRET_KEY'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}',
    SQLALCHEMY_ECHO = True
)

app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(player_routes, url_prefix='/api/player')

# Connect db to app
db.init_app(app)
Migrate(app, db)

# Application Security
CORS(app)

# Inject our csrf token to our response.
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if environ.get('FLASK_ENV') == 'production' else None, httponly=True)
    return response


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    # if path == 'favicon.ico':
    #     return app.send_from_directory('public', 'favicon.ico')
    return app.send_static_file('index.html')


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')
