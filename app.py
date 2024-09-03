from fastapi import FastAPI
from pydantic import BaseModel
from retriever import *

app = FastAPI()

retriever = Retriever(path_csv="./data/data_playlists_enem.csv", 
                      path_model='./models/tfidf_model_enem.pkl')

@app.get("/")
def read_root():
    return {"Status": "Running..."}

@app.get("/query")
def query(input_content: str):
    output = retriever.query(input_content, k=10)
    output_filtro = []
    for x in output:
        if x.relevance > 0.05:
            output_filtro.append(x)
    return {
        "results": output_filtro, 
        "message": "OK"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=1414)