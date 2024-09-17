from .logger import setup_logger

# Set up the logger for this module
logger = setup_logger(__name__)


def add(a, b):
    result = a + b
    logger.info(f"Adding {a} and {b}: {result}")
    return result


def subtract(a, b):
    result = a - b
    logger.info(f"Subtracting {b} from {a}: {result}")
    return result


def multiply(a, b):
    result = a * b
    logger.info(f"Multiplying {a} and {b}: {result}")
    return result
