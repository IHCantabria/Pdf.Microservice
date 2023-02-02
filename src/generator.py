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


class Generator(object):
    """_summary_

    Args:
        object (_type_): _description_
    """

    def __init__(self):
        """_summary_"""
        self.html_dir = self._get_a_copy_template()
        # self.annex = self._get_annex_text(self.job["refineryId"])

    def create(self, data: dict) -> Path:
        """Creates a pdf file from a dict

        Args:
            data (dict): fields to be used in the template

        Returns:
            Path: path to the pdf file
        """

        # generate map
        map = maps.generate_map(data["coords"], Path(self.html_dir, "imgs"))

        logger.debug("create using data: %s", data)
        index = f"{self.html_dir}/index.html"
        output_path = Path(os.getenv("OUTPUT_PDF_PATH"))

        env = Environment(loader=FileSystemLoader(self.html_dir))
        logger.debug("get template")
        template = env.get_template("index.html")

        varlist = data
        logger.debug("render template")
        index_html = template.render(varlist)
        logger.debug("render header")

        header_html = env.get_template("header.html").render()
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

    def _get_a_copy_template(self) -> Path:
        """Returns a copy of the template folder"""
        new_path = Path(tempfile.NamedTemporaryFile().name)
        logger.debug(f"Copying template to {new_path}")
        shutil.copytree(Path(os.getenv("TEMPLATE_PATH")), new_path)
        return new_path
