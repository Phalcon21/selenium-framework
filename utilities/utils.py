import inspect
import logging
import softest


class Utils(softest.TestCase):

    def custom_logger(logLevel: str = logging.DEBUG):
        # Set class/method name from where its called
        logger_name = inspect.stack()[1][3]
        # Create logger
        logger = logging.getLogger(logger_name)
        # Set level
        logger.setLevel(logLevel)
        # File handler
        fh = logging.FileHandler("reports/automation.log")
        # Formatting the logs
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        # Add file handler to logger
        logger.addHandler(fh)
        return logger
