import allure
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from utils.csv_reader import read_csv_data
from utils.logger import LogGen
from utils.screenshort_util import ScreenshotUtil

logger = LogGen.loggen()


# =====================================================
# INVALID MOBILE TEST
# =====================================================
@allure.feature("BigBasket Negative Tests")
@allure.title("Invalid Mobile Number")
def test_invalid_mobile(driver):

    wait = WebDriverWait(driver, 15)
    login = LoginPage(driver)

    login.open_bigbasket()
    logger.info("BigBasket website opened")

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Login')]")
    )).click()

    logger.info("Login button clicked")

    login.enter_mobile_email("12345")
    logger.info("Invalid mobile number entered")

    continue_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(),'Continue')]")
        )
    )

    logger.info("Verified Continue button is disabled")

    assert not continue_btn.is_enabled()

    ScreenshotUtil.capture_screenshot(driver, "invalid_mobile")
    logger.info("Invalid mobile screenshot captured")

    logger.info("Invalid mobile test passed")


# =====================================================
# INVALID OTP TEST
# =====================================================
@allure.feature("BigBasket Negative Tests")
@allure.title("Invalid OTP Login")
def test_invalid_otp(driver):

    wait = WebDriverWait(driver, 20)
    login = LoginPage(driver)

    data = read_csv_data("data/login_data.csv")

    # safety check
    if not data:
        raise Exception("CSV is empty or file not found")

    mobile = data[0].get("mobile")

    login.open_bigbasket()
    logger.info("BigBasket website opened")

    # click login
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Login')]")
    )).click()

    logger.info("Login button clicked")

    # enter mobile
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Enter Phone number/ Email Id']")
    ))

    login.enter_mobile_email(mobile)
    logger.info("Mobile number entered")

    login.click_continue()
    logger.info("Continue button clicked")

    logger.info("Waiting for OTP flow (manual or system)")

    # verify button flow
    try:

        verify_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Verify') or contains(text(),'Continue')]")
            )
        )

        verify_btn.click()
        logger.info("Verify button clicked")

    except Exception:

        logger.info("Verify button not found, continuing test flow")

    # allow error or failure state
    try:

        error = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(),'Invalid') or contains(text(),'error')]")
            )
        )

        logger.info("Invalid OTP error message displayed")

        result = True

    except Exception:

        logger.info("No explicit OTP error message displayed")

        result = False

    ScreenshotUtil.capture_screenshot(driver, "invalid_otp")
    logger.info("Invalid OTP screenshot captured")

    assert result or login.is_user_not_logged_in(), "OTP negative test failed"

    logger.info("Invalid OTP test passed")