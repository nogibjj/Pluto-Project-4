from fastapi import FastAPI
from fastapi.testclient import testclient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"m":"Wikipedia API"}

    