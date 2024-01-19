from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response =  client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Wellcome ! Go to Swagger Docs on /docs and have fun"}
