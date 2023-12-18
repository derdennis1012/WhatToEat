from flask import Blueprint
from flask import current_app as app

company_blueprint = Blueprint("company", __name__)

@company_blueprint.route("/", methods=["GET"])
def get():
    pass