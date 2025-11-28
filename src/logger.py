from loguru import logger
import sys
from src.config import DEBUG


def setup_logger():
    logger.remove()

    logger.add(
        sys.stderr, 
        level="DEBUG" if DEBUG else "INFO", 
        colorize=True, 
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | {message}", 
    )


    logger.add(
        "logs/app.log",
        level="DEBUG" if DEBUG else "INFO",
        rotation="1 MB",
        backtrace=DEBUG, 
        diagnose=DEBUG,
    )

    return logger

log = setup_logger() 