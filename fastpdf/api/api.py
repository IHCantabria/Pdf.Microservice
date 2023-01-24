import json
import shutil
import uuid
from pathlib import Path

from fastapi import APIRouter, Header
from fastapi.responses import FileResponse

from fastpdf.generator import Generator

router = APIRouter()




@router.get("/")
def create_pdf_demo(title:str="Título", content:str="Contenido"):
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
        })
    pdf_final_name = f"demo_{str(uuid.uuid4())}.pdf"
    pdf_final_path = Path(pdf.parent,pdf_final_name)
    shutil.move(pdf,pdf_final_path)
    return FileResponse(
        pdf_final_path,
        media_type="application/x-pdf",
        filename=pdf_final_name,
    )
