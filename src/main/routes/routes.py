from flask import Blueprint, request, jsonify

#import adapters
from src.main.adapters.request_adapter import request_adapter

#import composes 
from src.main.composers.user_finder_composer import user_composer_finder
from src.main.composers.user_register_composer import user_composer_register

# importt errors
from src.errors.error_handle import handle_error


user_routes_bp = Blueprint("users_routes", __name__)

@user_routes_bp.route("/user/find", methods=["GET"])
def find_user():
    http_response =None

    try:
        http_response = request_adapter(request,user_composer_finder())
    except Exception as exception:
        http_response = handle_error(exception)

    return jsonify(http_response.body), http_response.status_code



@user_routes_bp.route("/user", methods=["POST"])
def register_user():
    http_response = None
    try:
        http_response = request_adapter(request,user_composer_register())
    except Exception as exception:
        http_response = handle_error(exception) 
    
    return jsonify(http_response.body), http_response.status_code