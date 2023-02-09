import datetime
import logging
import logging.config
import os
from pathlib import Path


def get_logger(name: str) -> object:
    config_ini = Path(__file__).resolve().parent.parent / "logging.ini"

    fileh = logging.FileHandler(
        Path(os.getenv("LOG_DIR", "/app/logs/pdf"), "pdf.log"), "a"
    )

    logging.config.fileConfig(config_ini)

    # Cambiamos el path del fichero de log
    LOG_PATH = Path(os.getenv("LOG_DIR", "/app/logs/pdf"))
    if not LOG_PATH.exists():
        LOG_PATH.mkdir(parents=True)

    logger = logging.getLogger(name)
    file_handler = logger.parent.handlers[1]
    file_handler.close()
    file_handler.baseFilename = Path(LOG_PATH, "pdf.log")
    file_handler.flush()

    return logger


def datetime_to_string(date_obj: datetime.datetime, format="%Y-%m-%dT%H:%M:%SZ") -> str:
    return date_obj.strftime(format)


def string_to_datetime(
    str_date: str, format: str = "%Y-%m-%dT%H:%M:%SZ"
) -> datetime.datetime:
    return datetime.datetime.strptime(str_date, format)
