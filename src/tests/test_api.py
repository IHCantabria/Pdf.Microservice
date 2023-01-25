import pytest
import src.api.pdf_api


def test_check_download_pdf():
    response = src.api.pdf_api.create_pdf_demo(
        title="Título test", content="Contenido test"
    )
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/x-pdf"
    assert "demo_" in response.headers["Content-Disposition"]
