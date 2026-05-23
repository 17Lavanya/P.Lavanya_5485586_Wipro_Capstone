import allure

from utils.logger import LogGen

logger = LogGen.loggen()


class ScreenshotUtil:

    @staticmethod
    def capture_screenshot(driver, screenshot_name="screenshot"):

        allure.attach(
            driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=allure.attachment_type.PNG
        )

        logger.info(f"Screenshot attached in Allure report: {screenshot_name}")