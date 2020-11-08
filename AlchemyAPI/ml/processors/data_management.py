import requests
import json
import pandas as pd

def extract_data():
    url = 'http://api:5000/credits'
    headers = {"Content-Type": "application/json"}
    response_json = requests.get(url, headers=headers)
    data = json.loads(response_json.content)
    df = pd.json_normalize(data['credits'])
    df.drop(['id'], axis=1, inplace=True)

    print(f'Data extract successful! Num of elements: {df.shape[0]}')
    return df