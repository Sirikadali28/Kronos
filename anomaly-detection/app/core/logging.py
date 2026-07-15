import logging
import sys


def configure_logging() -> logging.Logger:
    """
    Configure the application logger.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
    )

    return logging.getLogger("kronos")