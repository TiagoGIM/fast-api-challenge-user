from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Wellcome ! Go to Swagger Docs on /docs and have fun"}