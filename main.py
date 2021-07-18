# pip install fastapi, uvicorn[standard]
# Run using cmd:  uvicorn main:app --reload
# http://127.0.0.1:8000/docs for API docs (swagger.ui)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Model Structure - Class
class ModelParams(BaseModel):
    name : str

@app.get('/')
def welcome():
    return "Hello"


#use any authentication to accept requests
@app.get('/get-model')
def getModel(): 
    return {"message": "aggregated model"}

@app.post("/send-model")
def sendModel(model: ModelParams):
    return {"message": model.name + ", cool!"}

