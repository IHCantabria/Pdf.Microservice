import json
import pytest
from fastapi.testclient import TestClient

import src.api.pdf_api
from src.main import app

client = TestClient(app)


def test_get_templates():
    response = client.get("/pdf/templates")
    assert response.status_code == 200
    assert response.json()["templates"] == ["ferrovial"]


def test_get_example():
    response = client.get("/pdf/example/ferrovial")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert (
        response.headers["content-disposition"]
        == 'attachment; filename="example-ferrovial.json"'
    )


def test_get_example_not_found():
    response = client.get("/pdf/example/ferrovial2")
    assert response.status_code == 404
    assert response.json() == "Template not found"


def test_create():
    response = client.post(
        "/pdf/create",
        json=json.load(open("templates/ferrovial/example.json")),
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/x-pdf"
    assert (
        "attachment" in response.headers["content-disposition"]
        and "pdf" in response.headers["content-disposition"]
    )
