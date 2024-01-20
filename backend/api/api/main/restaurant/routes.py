from flask import Blueprint
from flask import current_app as app
from flask_cors import cross_origin
from main.restaurant.models import Restaurant

restaurant_blueprint = Blueprint("restaurant", __name__)

@restaurant_blueprint.route("/<string:slug>", methods=["GET"])
def get(slug):
    return Restaurant().get(slug)

@restaurant_blueprint.route("/", methods=["POST"])
@cross_origin()
def add():
    return Restaurant().add()

@restaurant_blueprint.route("/<string:restaurantId>", methods=["DELETE"])
def delete(restaurantId):
    return Restaurant().delete(restaurantId)

@restaurant_blueprint.route("/all/", methods=["POST"])
@cross_origin()
def addAll():
    return Restaurant().addAll()    

@restaurant_blueprint.route("/all/", methods=["DELETE"])
def deleteAll():
    return Restaurant().deleteAll()

@restaurant_blueprint.route("/area/<int:area>/", methods=["GET"])
def getAllArea(area):
    return Restaurant().getArea(area)