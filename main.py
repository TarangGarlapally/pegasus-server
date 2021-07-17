from fastapi import FastAPI
from flask import render_template

app = FastAPI()

@app.get("/join")
def welcome():
    return "Hello"

@app.get("/home")
def home():
    return {"message": "hi"}


