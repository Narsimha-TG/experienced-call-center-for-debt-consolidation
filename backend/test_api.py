import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_analytics():
    response = client.get("/api/analytics")
    assert response.status_code == 200
    data = response.json()
    assert "total_leads" in data
    assert "avg_score" in data

def test_submit_review():
    payload = {
        "id": "3",
        "title": "Lead C",
        "status": "pending",
        "score": 75,
        "timestamp": "2023-10-27T10:00:00",
        "jornaya_token": "test_token",
        "trusted_form_cert": "test_cert",
        "lead_source_url": "http://example.com"
    }
    response = client.post("/api/reviews", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Data submitted successfully"

def test_approve_bid():
    response = client.post("/api/v1/bid/approve/6df220f1")
    assert response.status_code == 200
    assert response.json()["status"] == "success"