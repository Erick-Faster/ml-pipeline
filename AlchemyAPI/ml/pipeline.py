from creditrisk import Credit

class Pipeline:
    def create_pipeline(self):
        self.credit_risk = Credit()

    def ingest_data(self):
        self.credit_risk.ingest_data()

    def prepare_data(self):
        self.credit_risk.prepare_data()

    def train(self):
        self.credit_risk.train()

    def evaluate(self):
        self.credit_risk.evaluate()

    def deploy(self):
        self.credit_risk.deploy()
