from utils.waits import WaitUtils
from utils.logger import LogGen

logger = LogGen.loggen()


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator, name="Element"):
        element = WaitUtils.wait_for_element_clickable(
            self.driver,
            locator
        )
        element.click()
        logger.info(f"{name} clicked successfully")

    def enter_text(self, locator, text, name="Element"):
        element = WaitUtils.wait_for_element_visible(
            self.driver,
            locator
        )
        element.clear()
        element.send_keys(text)
        logger.info(f"Text entered in {name}: {text}")

    def get_text(self, locator, name="Element"):
        element = WaitUtils.wait_for_element_visible(
            self.driver,
            locator
        )
        text = element.text
        logger.info(f"Text fetched from {name}: {text}")
        return text

    def is_element_displayed(self, locator):
        try:
            element = WaitUtils.wait_for_element_visible(
                self.driver,
                locator
            )
            return element.is_displayed()
        except Exception:
            return False

    def safe_click(self, locator, name="Element"):
        try:
            self.click_element(locator, name)
            return True
        except Exception:
            logger.info(f"{name} not clickable or not available")
            return False