# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:32:03 2020

@author: erick
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

class Credit:
    def __init__(self):
        self.df_base = None
        self.df = None
        self.model = None

        self.X = None
        self.y = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

        self.y_pred = None
        self.accuracy = None
        self.confusion = None
        self.result = None


    def ingest_data(self):
        print('Begin Ingestion of Data')
        self.df_base = pd.read_csv('dags/german_credit_data.csv')
        self.df = self.df_base.iloc[:,1:]

    def prepare_data(self):

        # NaN Values
        self.df = self.df.fillna(value='no_data')

        # categorical columns

        self.df = pd.get_dummies(self.df, columns=['Sex', 'Housing', 'Saving accounts', 'Checking account', 'Purpose'], drop_first=True)

        self.X = self.df.drop(columns='Risk')
        self.y = self.df.loc[:,'Risk']

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.25, random_state=42)

    def train(self):
        self.model = RandomForestClassifier(random_state=27)
        self.model.fit(self.X_train,self.y_train)

    def evaluate(self):

        self.y_pred = self.model.predict(self.X_test)

        self.accuracy = accuracy_score(self.y_test, self.y_pred)
        self.confusion = confusion_matrix(self.y_test, self.y_pred)

    def deploy(self):
        self.result = {
            'accuracy': self.accuracy,
            'confusion': self.confusion
        }
        print(self.result)