import logging
import os
import shutil
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from src import utils
from src.PDFGenerator import PdfGenerator
from src import maps

logger = utils.get_logger(__name__)


class Generator:
    """_summary_

    Args:
        object (_type_): _description_
    """

    def __init__(self, template_name: str):
        """_summary_"""
        self.html_dir = self._get_a_copy_template(template_name)
        self.template_name = template_name
        # self.annex = self._get_annex_text(self.job["refineryId"])

    def create(self, data: dict) -> Path:
        """Creates a pdf file from a dict

        Args:
            data (dict): fields to be used in the template

        Returns:
            Path: path to the pdf file
        """

        # generate map
        # map = maps.generate_map(data["coords"], Path(self.html_dir, "imgs"))

        logger.debug("create using data: %s", data)
        # index = f"{self.html_dir}/{data['template_name']}/index.html"
        output_path = Path(os.getenv("OUTPUT_PDF_PATH"))

        env = Environment(loader=FileSystemLoader(self.html_dir))

        logger.debug("get template")
        template = env.get_template(Path(self.template_name, "index.html").as_posix())
        varlist = data.get("content")
        logger.debug("render template")
        index_html = template.render(varlist)

        logger.debug("render header")
        header_html = env.get_template(
            Path(self.template_name, "header.html").as_posix()
        ).render(varlist)

        logger.debug("pdfgenerator object")
        pdfgenerator = PdfGenerator(
            index_html, header_html=header_html, base_url=self.html_dir.as_posix()
        )
        logger.debug("render pdf")
        data = pdfgenerator.render_pdf()
        logger.debug("write pdf")
        with open(output_path, "wb") as f:
            f.write(data)
        logger.debug("delete temp")
        self.delete_temp()
        return output_path

    def delete_temp(self):
        """Deletes the temp folder"""
        try:
            shutil.rmtree(self.html_dir)  # En ocasiones da excepcion.
        except Exception as e:
            logger.warning(e.msg)

    def _calculate_simulation_hours(self, start, hours):
        date_start = utils.string_to_datetime(start)
        date_end = date_start + +timedelta(hours=hours)
        return date_end

    def _get_a_copy_template(self, template_name) -> Path:
        """Returns a copy of the template folder"""
        temp_preffix = os.getenv("TEMP_PREFFIX", "/tmp/")
        new_path = Path(tempfile.NamedTemporaryFile(prefix=temp_preffix).name)
        logger.debug(f"Copying template to {new_path}")
        shutil.copytree(Path(os.getenv("TEMPLATE_PATH", template_name)), new_path)
        return new_path

    def _validate_inputs(self, data):
        """Validates the inputs

        Args:
            data (dict): _description_

        Raises:
            Exception: _description_
        """
        if not data.get("project"):
            raise Exception("project name is required")
        if not data.get("content"):
            raise Exception("content is required")
