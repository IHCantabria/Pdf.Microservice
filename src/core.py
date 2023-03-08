from pathlib import Path
import os


def get_templates():
    """Returns a list of available templates"""
    templates = Path(os.getenv("TEMPLATE_PATH"))
    return [template.name for template in templates.iterdir() if template.is_dir()]
