import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from steps import Steps
import pickle

class Trainer:
    
    def __init__(self):
        self.steps = Steps()
        
    def collect(self):
        return pd.read_csv("./data/train.csv")
    
    def train(self, df):
        X = df.copy()
        y = X.pop("performance")
        
        X_train, _, y_train, _ = train_test_split(X, y, test_size=0.33, random_state=42)
        
        estimator = RandomForestClassifier(n_estimators=100, random_state=42)
        
        estimator.fit(X_train, y_train)
        
        return estimator
    
    def save(self, estimator):
        with open('./models/estimator.pkl', 'wb') as f:
            pickle.dump(estimator, f)
    
    def run(self):
        print("Collect")
        df = self.collect()
        
        print("Process")
        df = self.steps.process(df)
        
        print("Engineer")
        df = self.steps.engineer(df)
        
        print("Select")
        df = self.steps.select(df)
        
        print("Train")
        estimator = self.train(df)
        
        print("Save")
        self.save(estimator)
        print("Done!")