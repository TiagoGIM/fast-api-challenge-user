from fastapi import FastAPI
from .user.user_router import router_user
app = FastAPI()

app.include_router(router_user,prefix="/api")

@app.get("/")
def read_root():
    return {"msg": "Wellcome ! Go to Swagger Docs on /docs and have fun"}