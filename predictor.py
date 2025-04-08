import pickle

import pandas as pd
from steps import Steps

class Predictor:
    
    def __init__(self):
        self.estimator = None
        self.steps = Steps()
    
    def load(self):
        with open('./models/estimator.pkl', 'rb') as f:
            self.estimator = pickle.load(f)
    
    def predict(self, df):
        predictions = self.estimator.predict(df)
        
        predictions_df = pd.DataFrame(predictions, columns=["Predicted Price"])
        
        return predictions_df
        
    def run(self, df):
        self.load()
        
        df = self.steps.process(df)
        df = self.steps.engineer(df)
        df = self.steps.select(df, is_inference=True)
        
        predictions = self.predict(df)
        
        return predictions