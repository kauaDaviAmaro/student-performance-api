from fastapi import FastAPI, UploadFile, File
import pandas as pd
from predictor import Predictor
from trainer import Trainer
import io

app = FastAPI()

class APIService:
    def __init__(self):
        self.trainer = Trainer()
        self.predictor = Predictor()
        
    
    def isModelTrained(self):
        try:
            with open('./models/estimator.pkl', 'rb') as f:
                return True
        except FileNotFoundError:
            return False

    def init(self):
        isModelTrained = self.isModelTrained()
        
        if not isModelTrained:
            print("Treinando o modelo...")
            self.trainer.run()
            isModelTrained = True
        else:
            self.trainer.run()

    def predict(self, file: UploadFile):
        contents = file.file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        predictions = self.predictor.run(df)
        return predictions.to_dict(orient="records")

service = APIService()

# @app.post("/train")
# def train():
#     return service.init()

@app.post("/predict")
def predict(file: UploadFile = File(...)):
    return service.predict(file)
