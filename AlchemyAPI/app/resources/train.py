from flask import Flask
from flask_restful import Resource
import json
import requests

class Train(Resource):

    def get(self):
        url = 'http://127.0.0.1:6000/pipeline'
        headers = {"Content-Type": "application/json"}
        response_json = requests.get(url, headers=headers)
        response = json.loads(response_json.content)
        return response