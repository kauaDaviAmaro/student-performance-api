import pickle

import pandas as pd
from steps import Steps

class Predictor:
    
    def __init__(self):
        self.estimator = self.load()
        self.steps = Steps()
    
    def load(self):
        with open('./models/estimator.pkl', 'rb') as f:
            return pickle.load(f)
    
    def predict(self, estimator, df):
        predictions = estimator.predict(df)
        return predictions
        
    def run(self, df):        
        df = self.steps.process(df)
        df = self.steps.engineer(df)
        df = self.steps.select(df, is_inference=True)
        
        predictions = self.predict(self.estimator, df)
                
        return predictions