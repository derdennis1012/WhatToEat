from flask import Blueprint
from flask import current_app as app
from flask_cors import cross_origin
from main.votes.models import Votes

votes_blueprint = Blueprint("votes", __name__)

@votes_blueprint.route("/", methods=["GET"])
def get():
	return Votes().get()

@votes_blueprint.route("/", methods=["POST"])
@cross_origin()
def post():
	return Votes().post()

@votes_blueprint.route("/", methods=["DELETE"])
def delete():
    return Votes().delete()

@votes_blueprint.route("/<string:user_id>", methods=["GET"])
def getOne(user_id):
    return Votes().getOne(user_id)