from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

data = "Agartala"

@app.get("/")
def root():
    return {"Message": "Welcome to EC2 Test app"}

@app.get("/data")
def get_data():
    return {"Data": data}