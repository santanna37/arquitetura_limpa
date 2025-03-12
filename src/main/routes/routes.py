from flask import Blueprint, request, jsonify

#import adapters
from src.main.adapters.request_adapter import request_adapter

#import composes 
from src.main.composers.user_finder_composer import user_composer_finder
from src.main.composers.user_register_composer import user_composer_register



user_routes_bp = Blueprint("users_routes", __name__)

@user_routes_bp.route("/user/find", methods=["GET"])
def find_user():
    http_response = request_adapter(request,user_composer_finder())
    return jsonify(http_response.body), http_response.status_code


@user_routes_bp.route("/user", methods=["POST"])
def register_user():
    http_response = request_adapter(request,user_composer_register())

    return jsonify(http_response.body), http_response.status_code