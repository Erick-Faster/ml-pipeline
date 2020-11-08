import requests
import json
import pandas as pd
from instances import config

def extract_data(url):
    
    headers = {"Content-Type": "application/json"}
    response_json = requests.get(url, headers=headers)
    data = json.loads(response_json.content)
    df = pd.json_normalize(data['data'])
    df.drop(config.DROP_FEATURES, axis=1, inplace=True)

    print(f'Data extract successful! Num of elements: {df.shape[0]}')
    return df