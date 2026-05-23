import configparser
from utils.logger import LogGen


logger = LogGen.loggen()


class ConfigReader:

    config = configparser.ConfigParser()

    config.read("config/config.ini")

    @staticmethod
    def get_base_url():

        url = ConfigReader.config.get(
            "DEFAULT",
            "base_url"
        )

        logger.info("Base URL fetched")

        return url

    @staticmethod
    def get_browser():

        browser = ConfigReader.config.get(
            "DEFAULT",
            "browser"
        )

        logger.info("Browser fetched")

        return browser

    @staticmethod
    def get_timeout():

        timeout = ConfigReader.config.getint(
            "DEFAULT",
            "timeout"
        )

        logger.info("Timeout fetched")

        return timeout

    @staticmethod
    def get_implicit_wait():

        implicit_wait = ConfigReader.config.getint(
            "DEFAULT",
            "implicit_wait"
        )

        logger.info("Implicit wait fetched")

        return implicit_wait

    @staticmethod
    def get_headless():

        headless = ConfigReader.config.getboolean(
            "DEFAULT",
            "headless"
        )

        logger.info(
            f"Headless mode : {headless}"
        )

        return headless