import pytest
import os
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager

from utils.config_reader import ConfigReader
from utils.logger import LogGen

logger = LogGen.loggen()


# ==========================================
# SETUP FOLDERS
# ==========================================
def pytest_configure(config):

    os.makedirs("allure-results", exist_ok=True)
    os.makedirs("logs", exist_ok=True)


# ==========================================
# ALLURE ATTACHMENTS
# ==========================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    driver = item.funcargs.get("driver", None)

    # Attach for PASSED + FAILED tests
    if report.when == "call" and driver:

        # ==========================================
        # SCREENSHOT ATTACHMENT
        # ==========================================
        try:

            screenshot = driver.get_screenshot_as_png()

            allure.attach(
                screenshot,
                name=f"{item.name}_Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            logger.info("Screenshot attached to Allure report")

        except Exception as e:

            logger.error(f"Screenshot attach failed: {e}")

        # ==========================================
        # LOG FILE ATTACHMENT
        # ==========================================
        try:

            with open("logs/automation.log", "r") as log_file:

                allure.attach(
                    log_file.read(),
                    name="Automation Logs",
                    attachment_type=allure.attachment_type.TEXT
                )

            logger.info("Automation logs attached to Allure report")

        except Exception as e:

            logger.error(f"Log attach failed: {e}")


# ==========================================
# DRIVER FIXTURE
# ==========================================
@pytest.fixture(scope="function")
def driver():

    browser = ConfigReader.get("browser").strip().lower()
    headless = ConfigReader.get("headless").strip().lower() == "true"

    logger.info(f"Launching browser: {browser}")

    # ==========================================
    # CHROME SETUP
    # ==========================================
    if browser == "chrome":

        chrome_options = ChromeOptions()

        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")

        if headless:
            chrome_options.add_argument("--headless=new")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )

    # ==========================================
    # EDGE SETUP
    # ==========================================
    else:

        edge_options = EdgeOptions()

        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--disable-notifications")
        edge_options.add_argument("--disable-infobars")
        edge_options.add_argument("--disable-extensions")

        if headless:
            edge_options.add_argument("--headless")

        driver = webdriver.Edge(options=edge_options)

    driver.implicitly_wait(10)

    logger.info("Browser launched successfully")

    yield driver

    logger.info("Closing browser")

    driver.quit()

    logger.info("Browser closed successfully")