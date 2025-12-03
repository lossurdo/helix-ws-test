# main.py

from fastapi import FastAPI

# 1. Inicializa o aplicativo FastAPI
app = FastAPI()

# 2. Define um endpoint GET na raiz ("/")
@app.get("/")
def read_root():
    # Retorna um dicionário que o FastAPI converte em JSON
    return {"message": "Olá! Sua API FastAPI está rodando no Render! 🎉"}

# 3. Define um endpoint com um parâmetro de caminho
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "description": "Este é um item de exemplo."}

# Para rodar localmente, você usaria: uvicorn main:app --reload