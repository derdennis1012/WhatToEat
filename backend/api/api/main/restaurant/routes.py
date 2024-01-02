from flask import Blueprint
from flask import current_app as app

company_blueprint = Blueprint("restaurant", __name__)

@company_blueprint.route("/", methods=["GET"])
def get():
    pass