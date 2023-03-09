from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from src.api.pdf_api import router as router_pdf

from . import __version__

app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="PDF printer",
        version=__version__,
        description="Microservice to generate PDF files",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://ihcantabria.com/wp-content/uploads/2018/06/Logo-IHCantabria-Universidad-Cantabria_black-copia.jpg"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
app.include_router(router_pdf, prefix="/pdf", tags=["pdf"])
