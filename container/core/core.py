#This is the original file for the API_wrapper for Graphics-OS a
from fastapi import FastAPI
import uvicorn
import numpy as np

app = FastAPI()
@app.get('/')
def main():
    return {'message':'welcome to Graphic-OS'}

