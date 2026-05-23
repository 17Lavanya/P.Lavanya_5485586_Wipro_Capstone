import os
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from utils.config_reader import ConfigReader
from utils.logger import LogGen

logger = LogGen.loggen()


def before_all(context):
    os.makedirs(os.path.join(PROJECT_ROOT, "allure-results"), exist_ok=True)
    os.makedirs(os.path.join(PROJECT_ROOT, "logs"), exist_ok=True)


def before_scenario(context, scenario):
    browser = ConfigReader.get("browser").strip().lower()
    headless = ConfigReader.get("headless").strip().lower() == "true"

    logger.info(f"Launching browser for scenario: {scenario.name}")

    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")

        if headless:
            chrome_options.add_argument("--headless=new")

        context.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )
    else:
        edge_options = EdgeOptions()
        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--disable-notifications")
        edge_options.add_argument("--disable-infobars")
        edge_options.add_argument("--disable-extensions")

        if headless:
            edge_options.add_argument("--headless")

        context.driver = webdriver.Edge(options=edge_options)

    context.driver.implicitly_wait(int(ConfigReader.get("implicit_wait")))


def after_scenario(context, scenario):
    driver = getattr(context, "driver", None)

    if driver:
        if scenario.status == "failed":
            screenshot_dir = os.path.join(PROJECT_ROOT, "allure-results")
            screenshot_name = scenario.name.replace(" ", "_").lower() + ".png"
            driver.save_screenshot(os.path.join(screenshot_dir, screenshot_name))
            logger.info(f"Screenshot captured for failed scenario: {scenario.name}")

        logger.info(f"Closing browser for scenario: {scenario.name}")
        driver.quit()
