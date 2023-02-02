from pathlib import Path


from src.generator import Generator


path = Path(__file__).parent.parent


def test_create():
    generator = Generator()
    pdf = generator.create(
        {
            "title": "Hello World",
            "content": "This is a test",
            "coords": (-0.4577, 47.1104),
        }
    )
    assert pdf.exists()


if __name__ == "__main__":
    test_create()
