from flask import Flask
from flask_restful import Api
from pipeline import Pipeline

app = Flask(__name__)
app.secret_key = 'fast2'
api = Api(app)

api.add_resource(Pipeline, '/pipeline')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=False)