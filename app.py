from fastapi import FastAPI
from pydantic import BaseModel
from retriever import *

app = FastAPI()

retriever = Retriever(path_csv="./data/data_podcasts_title_content.csv", 
                      path_model='./models/tfidf_model.pkl')

class InputContent(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"Status": "Running..."}

@app.post("/query")
def query(input_content: InputContent):
    output = retriever.query(input_content.query, k=10)
    return output 