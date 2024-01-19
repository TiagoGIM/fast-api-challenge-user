from fastapi import FastAPI
from .user.user_router import router_user
from .authentication.auth_router import router_auth
app = FastAPI()

app.include_router(router_user,prefix="/api")
app.include_router(router_auth,prefix="/api")

@app.get("/")
def read_root():
    return {"msg": "Wellcome ! Go to Swagger Docs on /docs and have fun"}