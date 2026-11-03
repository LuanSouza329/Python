from fastapi import FastAPI, HTTPException

# Inicializa a API
app = FastAPI()

# Dados de exemplo mantidos em memória
usuarios = [
    {"id": 1, "nome": "Ana Silva", "status": "Ativo"},
    {"id": 2, "nome": "Bruno Costa", "status": "Ativo"},
    {"id": 3, "nome": "Carla Souza", "status": "Inativo"},
]


@app.get("/")
def home():
    return {"mensagem": "Minha API com FastAPI está online!"}


@app.get("/usuarios")
def listar_usuarios():
    return usuarios


@app.get("/usuarios/{usuario_id}")
def obter_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
