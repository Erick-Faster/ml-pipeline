

#App
HOST = '0.0.0.0'
PORT = 6000
DEBUG = False

#Extract Data
URL_DATA = 'http://api:5000/credits'

#Preprocessors
NUMERICAL_FEATURES = ['age', 'job', 'credit_amount' ,'duration']
CATEGORICAL_FEATURES = ['sex', 'housing', 'saving_accounts', 'checking_account', 'purpose']
DROP_FEATURES = ['id']
