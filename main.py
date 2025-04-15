from fastapi import FastAPI
import pandas as pd
from predictor import Predictor
from trainer import Trainer
from pydantic import BaseModel


app = FastAPI()

print("Starting the training process...")
tr = Trainer()
tr.run()
print("Training process completed.")

pr = Predictor()

class Item(BaseModel):
    gender: str
    race_ethnicity: str
    parental_level_of_education: str
    lunch: str
    test_preparation_course: str
    math_score: int
    reading_score: int
    writing_score: int
    
class ItemList(BaseModel):
    data: list[Item]

@app.post("/predict")
async def predict(data: ItemList):
    df = pd.DataFrame([item.dict() for item in data.data])
    pred = pr.run(df)

    print(pred)
    return {"predictions": pred.tolist()}