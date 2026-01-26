from fastapi.testclient import TestClient
from app.main import app  # adjust if your entry file is different

client = TestClient(app)

def test_health_check():
    response = client.get("/home")
    assert response.status_code == 200
