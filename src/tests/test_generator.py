import json
from pathlib import Path

from src.generator import Generator

path = Path(__file__).parent.parent


def test_create():
    generator = Generator("ferrovial")
    pdf = generator.create(json.load(open("templates/ferrovial/example.json")))
    assert pdf.exists()


if __name__ == "__main__":
    test_create()
