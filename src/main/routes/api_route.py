from flask import Blueprint, jsonify

api_route_bp = Blueprint("api_route", __name__)


@api_route_bp.route("/api", methods=["GET"])
def something():
    """teste"""

    return jsonify({"Success": True})
