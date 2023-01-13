import logging
import logging.config
from pathlib import Path


def get_logger(name: str) -> object:
    config_ini = Path(__file__).resolve().parent.parent / "logging.ini"
    logging.config.fileConfig(config_ini)
    logger = logging.getLogger(name)
    return logger
