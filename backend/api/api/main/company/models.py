from flask import current_app as app
from flask import Flask, request
from jose import jwt
from main import tools

class company:
    def __init__(self):
        self.defaults = {
            "id": tools.randID(),
            "ip_addresses": [request.remote_addr],
            "acct_active": True,
            "date_created": tools.nowDatetimeUTC(),
            "last_login": tools.nowDatetimeUTC(),
            "first_name": "",
            "last_name": "",
            "email": "",
            #comany reference to the company collection
            "company": "",
        }
