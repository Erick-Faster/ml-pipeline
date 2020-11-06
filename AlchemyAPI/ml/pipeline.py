from creditrisk import Credit
from flask_restful import Resource, reqparse

class Pipeline(Resource):

    def get(self):
        credit_risk = Credit()
        credit_risk.ingest_data()
        credit_risk.prepare_data()
        credit_risk.train()
        credit_risk.evaluate()
        credit_risk.deploy()

        return {
            "results": credit_risk.result
        }
