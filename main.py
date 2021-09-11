# pip install fastapi, uvicorn[standard]
# Run using cmd:  uvicorn main:app --reload
# http://127.0.0.1:8000/docs for API docs (swagger.ui)

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
import services

app = FastAPI()

# Model Structure - Class
class ModelParams(BaseModel):
    email: str
    classes_: List[float]
    coef_: List[List[float]]
    intercept_: List[float]
    n_iter_: List[int]

@app.get('/')
def welcome():
    return "Hello"


#use any authentication to accept requests
@app.post('/get-score')
def getModel(model: Dict[Any, Any] = None): 
    return {"score": services.calculateScore(model)}
