from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

app = Flask(__name__)

MONGODB_URI = "mongodb://root:WaRa_bestSchool%40wrld!@localhost:27017/flask_db?authSource=admin"
client = MongoClient(MONGODB_URI)


db = client.WhatToEat
stores = db.stores

#port 5555


@app.route("/")
def index():
    return "Hello World"
