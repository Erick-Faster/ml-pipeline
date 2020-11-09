# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:17:25 2020

@author: erick
"""

import boto3
from botocore.exceptions import NoCredentialsError

def download_from_aws(down_file, bucket, s3_file):


    s3 = boto3.client('s3', aws_access_key_id='AKIA4FUG32ISCSDAWHYZ',
                      aws_secret_access_key='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')
    try:
        s3.download_file(bucket, s3_file, down_file)
        print("Download Successful")
        return True
    except FileNotFoundError:
        print ("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not avaliable")
        return False
    
    
def upload_to_aws(local_file, bucket, s3_file):
    
    s3 = boto3.client('s3', aws_access_key_id='AKIA4FUG32ISCSDAWHYZ',
                      aws_secret_access_key='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')
    
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print ("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not avaliable")
        return False



download_from_aws(down_file, bucket, s3_file)
upload_to_aws(local_file, bucket, s3_file)

filepath = 'models/rf'

def save_pickle(filepath, objeto, use_date=False):
    
    if use_date:
        date = datetime.now().strftime("-%Y-%m-%dT%H-%M-%S-%f")
        filepath = f'{filepath}{date}'
    outfile = open(f'{filepath}.pkl','wb')
    pickle.dump(objeto,outfile)
    outfile.close()


from datetime import datetime
modelname = datetime.now().strftime("rf-%Y-%m-%dT%H-%M-%S-%f")
modelname = 
folder = "classifiers/"+foldername