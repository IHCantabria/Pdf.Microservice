import pytest
from src import maps
from pathlib import Path


def test_get_map():
    map = maps.generate_map((-0.4577, 47.1104), Path("/tmp"))
    assert map.exists()


def test_check_valid_center():
    with pytest.raises(ValueError):
        maps._check_valid_center((1000, 1000))
    with pytest.raises(TypeError):
        maps._check_valid_center(("5", "47"))

    # Should not raise
    maps._check_valid_center((-5, -47))


def test_check_path_exists():
    with pytest.raises(FileNotFoundError):
        maps._check_path_exists(Path("/tmp/does_not_exist"))

    # Should not raise
    maps._check_path_exists(Path("/tmp"))
