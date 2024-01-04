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

@restaurant_blueprint.route("/", methods=["DELETE"])
def delete():
    return Restaurant().delete()

@restaurant_blueprint.route("/all/", methods=["GET"])
def getAll():
    return Restaurant().getAll()

@restaurant_blueprint.route("/all/", methods=["POST"])
def addAll():
    return Restaurant().addAll()    

@restaurant_blueprint.route("/all/", methods=["DELETE"])
def deleteAll():
    return Restaurant().deleteAll()