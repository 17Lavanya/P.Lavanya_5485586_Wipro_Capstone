from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.config_reader import ConfigReader


class WaitUtils:

    timeout_duration = ConfigReader.get_timeout()

    @staticmethod
    def wait_for_element_visible(driver, locator, timeout=timeout_duration):
        try:
            return WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise

    @staticmethod
    def wait_for_element_clickable(driver, locator, timeout=timeout_duration):
        try:
            return WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            raise

    @staticmethod
    def wait_for_presence_of_element(driver, locator, timeout=timeout_duration):
        try:
            return WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise

    @staticmethod
    def wait_for_title_contains(driver, title, timeout=timeout_duration):
        try:
            return WebDriverWait(driver, timeout).until(
                EC.title_contains(title)
            )
        except TimeoutException:
            raise

    @staticmethod
    def wait_for_alert(driver, timeout=timeout_duration):
        try:
            return WebDriverWait(driver, timeout).until(
                EC.alert_is_present()
            )
        except TimeoutException:
            raise

    @staticmethod
    def wait_for_invisibility(driver, locator, timeout=timeout_duration):
        try:
            return WebDriverWait(driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            raise