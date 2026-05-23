from behave import when, then
from selenium.webdriver.common.by import By
import allure

from locators.login_locators import LoginLocators
from utils.logger import LogGen
from utils.waits import WaitUtils
from utils.screenshort_util import ScreenshotUtil

import time

logger = LogGen.loggen()


@when('user enters invalid mobile number "{mobile}"')
def step_enter_invalid_mobile(context, mobile):

    with allure.step("Enter invalid mobile number"):
        context.login_page.enter_mobile_email(mobile)
        logger.info(f"Invalid mobile number entered: {mobile}")


@then("continue button should be disabled")
def step_validate_continue_disabled(context):

    with allure.step("Validate Continue button is disabled"):

        continue_button = WaitUtils.wait_for_presence_of_element(
            context.driver,
            (By.XPATH, "//button[contains(text(),'Continue')]")
        )

        assert not continue_button.is_enabled(), \
            "Continue button should be disabled"

        ScreenshotUtil.capture_screenshot(
            context.driver,
            "invalid_mobile"
        )

        logger.info("Continue button is disabled as expected")


@when("user waits for manual invalid OTP entry")
def step_wait_for_manual_invalid_otp(context):

    with allure.step("Wait for manual invalid OTP entry"):

        logger.info("Waiting for user to enter invalid OTP manually")

        WaitUtils.wait_for_element_clickable(
            context.driver,
            LoginLocators.VERIFY_BUTTON,
            timeout=200
        )

        logger.info("Verify button is clickable after OTP entry")


@then("invalid OTP error message should be displayed")
def step_validate_invalid_otp_error(context):

    with allure.step("Validate invalid OTP error message"):

        WaitUtils.wait_for_element_visible(
            context.driver,
            LoginLocators.OTP_ERROR,
            timeout=200
        )

        time.sleep(5)

        error_message = context.login_page.get_otp_error_message()

        assert error_message, "OTP error message not displayed"

        assert (
                "enter otp" in error_message.lower()
                or "please enter valid otp" in error_message.lower()
        ), "Invalid OTP validation failed"

        allure.attach(
            error_message,
            name="OTP Error Message",
            attachment_type=allure.attachment_type.TEXT
        )

        ScreenshotUtil.capture_screenshot(
            context.driver,
            "invalid_otp"
        )

        logger.info(
            "Invalid OTP validation message displayed successfully"
        )

        time.sleep(3)