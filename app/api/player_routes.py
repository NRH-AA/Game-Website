from flask import Blueprint, jsonify, session, request
from app.models import db, User, Player
from flask_login import current_user, login_user, logout_user, login_required

player_routes = Blueprint('player', __name__)

@player_routes.route('/', methods=['GET'])
def get_all_players():
    players = Player.query.all() 
    return [player.to_dict() for player in players]
