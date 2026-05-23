import os
import allure

from utils.logger import LogGen
from utils.config_reader import ConfigReader
from utils.screenshort_util import ScreenshotUtil

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions

logger = LogGen.loggen()


def before_scenario(context, scenario):

    log_file = "logs/automation.log"

    if os.path.exists(log_file):
        open(log_file, "w").close()

    context.step_count = 0
    context.total_steps = len(scenario.steps)

    logger.info("========================================")
    logger.info(f"Starting scenario: {scenario.name}")

    feature_file = scenario.filename.lower()

    allure.dynamic.parent_suite("features")

    if "end_to_end" in feature_file:
        allure.dynamic.suite("end_to_end")

    elif "negative" in feature_file:
        allure.dynamic.suite("negative")

    elif "positive" in feature_file:
        allure.dynamic.suite("positive")

    else:
        allure.dynamic.suite("other")

    allure.dynamic.sub_suite(
        scenario.feature.name
    )

    browser = ConfigReader.get_browser()
    base_url = ConfigReader.get_base_url()
    implicit_wait = ConfigReader.get_implicit_wait()
    headless = ConfigReader.get_headless()

    if browser.lower() == "chrome":

        chrome_options = Options()

        chrome_options.add_argument(
            "--disable-notifications"
        )

        chrome_options.add_argument(
            "--disable-infobars"
        )

        chrome_options.add_argument(
            "--disable-extensions"
        )

        if headless:
            chrome_options.add_argument(
                "--headless"
            )

        context.driver = webdriver.Chrome(
            options=chrome_options
        )

    elif browser.lower() == "edge":

        edge_options = EdgeOptions()

        edge_options.add_argument(
            "--disable-notifications"
        )

        edge_options.add_argument(
            "--disable-infobars"
        )

        edge_options.add_argument(
            "--disable-extensions"
        )

        if headless:
            edge_options.add_argument(
                "--headless"
            )

        context.driver = webdriver.Edge(
            options=edge_options
        )

    else:

        logger.error(
            f"Unsupported browser: {browser}"
        )

        context.driver = webdriver.Edge(
            options=EdgeOptions()
        )

    context.driver.maximize_window()

    context.driver.implicitly_wait(
        implicit_wait
    )

    context.driver.get(base_url)

    logger.info(
        "Browser launched successfully"
    )


def after_step(context, step):

    try:

        context.step_count += 1

        if context.step_count <= context.total_steps:

            screenshot_name = (
                step.name.replace(" ", "_")
            )

            ScreenshotUtil.capture_screenshot(
                context.driver,
                screenshot_name
            )

    except Exception as e:

        logger.info(
            f"Step screenshot skipped: {e}"
        )


def after_scenario(context, scenario):

    log_file = "logs/automation.log"

    if os.path.exists(log_file):

        allure.attach.file(
            log_file,
            name="Logs",
            attachment_type=allure.attachment_type.TEXT
        )

    if scenario.status == "failed":

        ScreenshotUtil.capture_screenshot(
            context.driver,
            scenario.name
        )

        logger.error(
            f"Scenario failed: {scenario.name}"
        )

    else:

        logger.info(
            f"Scenario passed: {scenario.name}"
        )

    context.driver.quit()

    logger.info(
        "Browser closed successfully"
    )

    logger.info(
        "========================================"
    )