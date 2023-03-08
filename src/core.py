from pathlib import Path
import os


def get_templates():
    """Returns a list of available templates"""
    templates = Path(os.getenv("TEMPLATE_PATH"))
    return [template.name for template in templates.iterdir() if template.is_dir()]


def get_example(template_name):
    """Returns a JSON file with the given title and content."""
    example_path = Path(os.getenv("TEMPLATE_PATH"), template_name, "example.json")
    return example_path
