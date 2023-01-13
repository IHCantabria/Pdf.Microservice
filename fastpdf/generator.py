import logging
import os
import shutil
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from weasyprint import CSS, HTML

from fastpdf import utils
from fastpdf.PDFGenerator import PdfGenerator

logger = utils.get_logger(__name__)


class Generator(object):
    def __init__(self):
        self.html_dir = self._get_a_copy_template()
        # self.annex = self._get_annex_text(self.job["refineryId"])

    def create(self):

        index = f"{self.html_dir}/index.html"
        output = f"/tmp/Report.pdf"

        env = Environment(loader=FileSystemLoader(self.html_dir))
        template = env.get_template("index.html")

        varlist = {
            "title": "variable_titulo",
            "annex": "texto anexo",
        }
        index_html = template.render(varlist)

        header_html = env.get_template("header.html").render()

        pdfgenerator = PdfGenerator(
            index_html, header_html=header_html, base_url=self.html_dir
        )
        data = pdfgenerator.render_pdf()
        f = open(output, "wb")
        f.write(data)
        f.close()

        return output

    def delete_temp(self):
        try:
            shutil.rmtree(self.html_dir)  # En ocasiones da excepcion.
        except Exception as e:
            logger.warning(e.msg)

    def _calculate_simulation_hours(self, start, hours):
        date_start = utils.string_to_datetime(start)
        date_end = date_start + +timedelta(hours=hours)
        return date_end

    def _get_a_copy_template(self):
        new_path = tempfile.NamedTemporaryFile().name
        logger.debug(f"Copying template to {new_path}")
        shutil.copytree(os.getenv("TEMPLATE_PATH"), new_path)
        return new_path
