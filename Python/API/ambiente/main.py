from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def hello_root():
    return {"message": "Hello World"}

#uvicorn ambiente.main:app --reload // comando para rodar o ambiente