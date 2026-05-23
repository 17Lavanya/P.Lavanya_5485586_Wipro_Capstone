import logging
import os


class LogGen:

    @staticmethod
    def loggen():

        log_dir = "logs"

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logger = logging.getLogger("Automation")

        logger.setLevel(logging.INFO)

        # prevent duplicate handlers
        if logger.hasHandlers():
            logger.handlers.clear()

        file_handler = logging.FileHandler(
            "logs/automation.log",
            mode="w"
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger