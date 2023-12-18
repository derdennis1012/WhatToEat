from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient
from main.tools import JsonResp
from jose import jwt
import os
from bson.objectid import ObjectId


# Import Routes
from main.user.routes import user_blueprint

def create_app():

  # Flask Config
  app = Flask(__name__)
  app.config.from_pyfile("config/config.cfg")
  cors = CORS(app, resources={r"/*": { "origins": app.config["FRONTEND_DOMAIN"] }})
  app.config['CORS_HEADERS'] = 'Content-Type'

  # Misc Config
  os.environ["TZ"] = app.config["TIMEZONE"]

  #mongodb uri mongodb://root:WaRa_bestSchool%40wrld!@localhost:27017/?authSource=admin
  MONGODB_URI = "mongodb://root:WaRa_bestSchool%40wrld!@localhost:27017/flask_db?authSource=admin"
  client = MongoClient(MONGODB_URI)


  db = client.WhatToEat
  app.db = db
  app.client = client
  app.ObjectId = ObjectId
  print("db", db.users.count_documents({}))



  # Register Blueprints
  app.register_blueprint(user_blueprint, url_prefix="/user")

  # Index Route
  @app.route("/")
  def index():
    return JsonResp({ "status": "Online" }, 200)
  
  return app