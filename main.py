# pip install fastapi
# pip install uvicorn
# para rodar => uvicorn main:app --reload

from fastapi import FastAPI
from pydantic import BaseModel


class Usuario(BaseModel):
    id: int
    email: str
    senha: str


base_de_dados = [
    Usuario(id=1, email="milton@gmail.com", senha="milton123"),
    Usuario(id=2, email="lucas@gmail.com", senha="lucas123"),
]


app = FastAPI()


@app.get("/")
def raiz():
    return {"Ola": "Mundo"}


@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados

@app.get("/usuarios/{id}")
def get_usuario_por_id(id: int):
    for usuario in base_de_dados:
        if usuario.id == id:
            return usuario

    return {"status": 404, "message": f'usuário {id} não encontrado'}

@app.post('/usuarios')
def insere_usuario(usuario: Usuario):
    base_de_dados.append(usuario)