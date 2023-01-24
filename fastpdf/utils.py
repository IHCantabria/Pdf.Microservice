import datetime
import logging
import logging.config
from pathlib import Path


def get_logger(name: str) -> object:
    config_ini = Path(__file__).resolve().parent.parent / "logging.ini"
    logging.config.fileConfig(config_ini)
    logger = logging.getLogger(name)
    return logger


def datetime_to_string(date_obj: datetime.datetime, format="%Y-%m-%dT%H:%M:%SZ") -> str:
    return date_obj.strftime(format)


def string_to_datetime(
    str_date: str, format: str = "%Y-%m-%dT%H:%M:%SZ"
) -> datetime.datetime:
    return datetime.datetime.strptime(str_date, format)
