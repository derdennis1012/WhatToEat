from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient
from main.tools import JsonResp
from jose import jwt
import os
from bson.objectid import ObjectId


# Import Routes
from main.restaurant.routes import restaurant_blueprint
from main.votes.routes import votes_blueprint

def create_app():

  # Flask Config
  app = Flask(__name__)
  app.config.from_pyfile("config/config.cfg")
  cors = CORS(app, resources={r"/*": { "origins": app.config["FRONTEND_DOMAIN"] }})
  app.config['CORS_HEADERS'] = 'Content-Type'

  # Misc Config
  os.environ["TZ"] = app.config["TIMEZONE"]

  MONGODB_URI = f"""{app.config['MONGO_CONNECTION_TYPE']}://{app.config['MONGO_AUTH_USERNAME']}:{app.config['MONGO_AUTH_PASSWORD']}@
                {app.config['MONGO_HOSTNAME']}/flask_db?authSource={app.config['MONGO_AUTH_DATABASE']}"""
  
  client = MongoClient(MONGODB_URI)


  db = client.WhatToEat
  app.db = db
  app.client = client
  app.ObjectId = ObjectId
  print("db", db.users.count_documents({}))



  # Register Blueprints
  app.register_blueprint(restaurant_blueprint, url_prefix="/restaurant")
  app.register_blueprint(votes_blueprint, url_prefix="/votes")  

  # Index Route
  @app.route("/")
  def index():
    return JsonResp({ "status": "Online" }, 200)
  
  return app