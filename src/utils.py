import logging
from datetime import datetime


def get_logger(name: str) -> logging.Logger:
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(name)


def current_timestamp_str() -> str:
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")