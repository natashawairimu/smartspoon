 # debug.py

import logging

# Configure logging to write to console with timestamp and level
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_debug(message):
    """Log a debug message"""
    logging.debug(message)

def log_info(message):
    """Log an info message"""
    logging.info(message)

def log_warning(message):
    """Log a warning message"""
    logging.warning(message)

def log_error(message):
    """Log an error message"""
    logging.error(message)
