from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Olá! Sua API FastAPI está rodando no Render! 🎉"}


@app.get("/rest/info")
def info():
    return {
        "message": "ok"
    }