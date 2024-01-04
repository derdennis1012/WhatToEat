from flask import Blueprint
from flask import current_app as app
from main.restaurant.models import Restaurant

restaurant_blueprint = Blueprint("restaurant", __name__)

@restaurant_blueprint.route("/", methods=["GET"])
def get():
    return Restaurant().get()

@restaurant_blueprint.route("/", methods=["POST"])
def add():
    return Restaurant().add()