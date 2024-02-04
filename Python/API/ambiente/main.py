from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def hello_root():
    return {"message": "Hello World"}

@app.get("/teste")

def hello_teste():
    return {"message": "Testando rotas"}


#uvicorn ambiente.main:app --reload // comando para rodar o ambiente