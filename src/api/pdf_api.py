import shutil
import uuid
from pathlib import Path

from fastapi import APIRouter, Header
from fastapi.responses import FileResponse

from src.generator import Generator

router = APIRouter()


def create_pdf_demo(title: str = "Título", content: str = "Contenido"):
    """Returns a PDF file with the given title and content.

    Args:
        title (str, optional): _description_. Defaults to "Título".
        content (str, optional): _description_. Defaults to "Contenido".

    Returns:
        _type_: _description_
    """

    generator = Generator()
    pdf = generator.create(
        {
            "title": "Hello World",
            "content": "This is a test",
            "coords": (-0.4577, 47.1104),
        }
    )
    pdf_final_name = f"demo_{str(uuid.uuid4())}.pdf"
    pdf_final_path = Path(pdf.parent, pdf_final_name)
    shutil.move(pdf, pdf_final_path)
    return FileResponse(
        pdf_final_path,
        media_type="application/x-pdf",
        filename=pdf_final_name,
    )


@router.post("/create")
def create_pdf(data: dict):
    """Returns a PDF file"""
    generator = Generator(data["template_name"])
    pdf = generator.create(data)
    pdf_final_name = f"{str(uuid.uuid4())}.pdf"
    pdf_final_path = Path(pdf.parent, pdf_final_name)
    shutil.move(pdf, pdf_final_path)
    return FileResponse(
        pdf_final_path,
        media_type="application/x-pdf",
        filename=pdf_final_name,
    )
    # return pdf_final_path
