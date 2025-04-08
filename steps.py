from sklearn.preprocessing import LabelEncoder
import pandas as pd

class Steps:
    def process(self, df):
        # Placeholder for data processing steps
        return df
    
    def engineer(self, df):        
        obj_cols = df.select_dtypes(include=['object']).columns
        
        for col in obj_cols:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            
        df["performance"] = df[["math score", "reading score", "writing score"]].mean(axis=1) > 60
        
        return df
    
    def select(self, df, is_inference=False):
        sel_col = ['gender',
            'race/ethnicity',
            'parental level of education',
            'lunch',
            'test preparation course',
            'math score',
            'reading score',
            'writing score',
            'performance', # target variable
        ]
        
        if is_inference:
            sel_col.remove('performance')
        
        return df[sel_col]