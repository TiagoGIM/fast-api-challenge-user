from fastapi import FastAPI
from .user.user_router import router_user
from .authentication.auth_router import router_auth

description = """
### Users
É possivel realizar todas as operações básicas do CRUD.
Porém algumas rotas necessitam de autorização
### Security
Recurso que permite gerar tokens para Usuários cadastrados.
"""
app = FastAPI(
    title= "API de Gestão de usuários",
    summary="API to manager a user CRUD",
    description=description,
    version="0.0.1",
)

app.include_router(router_user,prefix="/api")
app.include_router(router_auth,prefix="/api")

@app.get("/")
def read_root():
    return {"msg": "Wellcome ! Go to Swagger Docs on /docs and have fun"}