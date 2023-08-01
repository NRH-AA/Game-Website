from flask import Blueprint, request
from flask_login import login_required
from app.models import db, User
from sqlalchemy import desc, asc
from app.utils import (
    upload_file_to_s3, allowed_file, get_unique_filename)

user_routes = Blueprint('users', __name__)

# Get specific user information
# /api/users/user_id
@user_routes.route('/<int:id>', methods=['GET'])
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()

# Change user theme
# /api/users/user_id/theme
@user_routes.route('/<int:id>/theme', methods=['POST'])
@login_required
def update_user_theme(id):
    data = request.get_json()
    theme = data['theme']
    
    user = User.query.get(id)
    user.theme = theme
    
    db.session.commit()
    ret = User.query.get(id)
    
    return ret.to_dict()

# Change user profile picture
# /api/users/user_id/picture
@user_routes.route('/<int:id>/picture', methods=['POST'])
@login_required
def update_user_picture(id):
    profile_picture = request.get_json()['profile_picture']
    
    if not profile_picture:
        return {'errors': ['Failed to get profile picture']}, 400
    
    user = User.query.get(id)
    user.profile_picture = profile_picture
    db.session.commit()
    ret = User.query.get(id)
    return ret.to_dict()

# Upload an image to S3 bucket (required for user profile pictures)
# /api/users/upload
@user_routes.route('/upload', methods=['POST'])
@login_required
def upload_image():
    if "image" in request.files:
        image = request.files["image"]

    if not allowed_file(image.filename):
        return {"errors": "file type not permitted"}, 400

    image.filename = get_unique_filename(image.filename)

    upload = upload_file_to_s3(image)

    if "url" not in upload:
        return upload, 400

    imageURL = upload["url"]
    return {"url": imageURL}
