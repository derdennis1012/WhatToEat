from flask import current_app as app
from flask import Flask, request
from main import tools
from bson.json_util import dumps
import json

class Votes:
    def __init__(self):
        self._defaults = {
            "restaurant_slug": "",
            "user_id": ""
        }

    def post(self):
        data = json.loads(request.data)
        expected_data = {
            "restaurant_slug": data["restaurant_slug"],
            "user_id": data["user_id"]
        }
        self._defaults.update(expected_data)
        vote = app.db.votes.find_one({"user_id": self._defaults["user_id"]})
        if vote:
            app.db.votes.update_one({"user_id": self._defaults["user_id"]}, {"$set": self._defaults})
            resp = tools.JsonResp({"message": "Vote updated"}, 200)
        else:
            app.db.votes.insert_one(self._defaults)
            resp = tools.JsonResp({"message": "Vote added"}, 200)
        return resp
        
    def get(self):
        voteCount = {}
        cursor = app.db.votes.find({})
        list_cur = list(cursor)
        votes = json.loads(dumps(list_cur))
        for vote in votes:
            if vote["restaurant_slug"] in voteCount:
                voteCount[vote["restaurant_slug"]] += 1
            else:
                voteCount[vote["restaurant_slug"]] = 1   
        resp = tools.JsonResp(voteCount, 200)
        return resp
    
    def getOne(self, user_id):
        vote = app.db.votes.find_one({"user_id": user_id})
        if vote:
            vote.pop("_id", None)
            resp = tools.JsonResp(vote, 200)
        else:
            resp = tools.JsonResp({"message": "Vote not found"}, 404)
        return resp

    def delete(self):   
        if app.db.votes.delete_many({}):
            resp = tools.JsonResp({"message": "All votes deleted"}, 200)
        else:
            resp = tools.JsonResp({"message": "No votes to delete"}, 400)    
        return resp        