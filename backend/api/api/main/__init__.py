from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient
from main.tools import JsonResp
#from jose import jwt
import os
from bson.objectid import ObjectId


# Import Routes
#from main.user.routes import user_blueprint
from main.restaurant.routes import restaurant_blueprint
from main.votes.routes import votes_blueprint

def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

def create_app():

  # Flask Config
  app = Flask(__name__)
  app.config.from_pyfile("config/config.cfg")
  # enable cors for all domains on all routes so allow everything for dev
  cors = CORS(app, resources={r"/*": {"origins": "*"}})
  app.config['CORS_HEADERS'] = 'Content-Type'
  # Misc Config
  os.environ["TZ"] = app.config["TIMEZONE"]
  app.after_request(after_request)
  CORS(app)


  MONGODB_URI = "mongodb+srv://root:Wara_bestSchool%40wrld!@whattoeat.vbsty6v.mongodb.net/flask_db?authSource=admin"
  #print the connection string we will use to connect to MongoDB
  print(MONGODB_URI)

  client = MongoClient(MONGODB_URI)


  db = client.WhatToEat
  app.db = db
  app.client = client
  app.ObjectId = ObjectId
  print("db", db.users.count_documents({}))



  # Register Blueprints
  #app.register_blueprint(user_blueprint, url_prefix="/user")
  app.register_blueprint(restaurant_blueprint, url_prefix="/restaurant")
  app.register_blueprint(votes_blueprint, url_prefix="/votes")  

  # Index Route
  @app.route("/")
  def index():
    return JsonResp({ "status": "Online" }, 200)
  
  return app