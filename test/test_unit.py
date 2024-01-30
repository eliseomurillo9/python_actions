from fastapi.testclient import TestClient
import pytest
from application.main import app
from random import randint

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World!"