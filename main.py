
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg" : "vanakkam da mapla"}

@app.get('/health')
def health():
    return {"msg": "working"}