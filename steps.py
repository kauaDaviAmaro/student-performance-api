from sklearn.preprocessing import LabelEncoder
import pandas as pd

class Steps:
    def process(self, df):
        df.columns = df.columns.str.replace(' ', '_')
        if 'race_ethnicity' in df.columns:
            df.rename(columns={'race_ethnicity': 'race/ethnicity'}, inplace=True)
            
        return df
    
    def engineer(self, df):        
        obj_cols = df.select_dtypes(include=['object']).columns
        
        for col in obj_cols:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            
        df["performance"] = df[["math_score", "reading_score", "writing_score"]].mean(axis=1) > 60
        
        return df
    
    def select(self, df, is_inference=False):
        sel_col = ['gender',
            'race/ethnicity',
            'parental_level_of_education',
            'lunch',
            'test_preparation_course',
            'math_score',
            'reading_score',
            'writing_score',
            'performance', # target variable
        ]
        
        if is_inference:
            sel_col.remove('performance')
        
        return df[sel_col]