from fastapi.testclient import TestClient
from . import main

def test_endpoint():
    t = TestClient(main.app)

    r = t.get("/health")
    assert r.status_code == 200
    assert r.json()['endpoint'] == 'health'