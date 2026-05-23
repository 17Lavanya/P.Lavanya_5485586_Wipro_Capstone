from locators.login_locators import LoginLocators
from pages.base_page import BasePage
from utils.csv_reader import read_csv_data
from utils.logger import LogGen
from utils.waits import WaitUtils

logger = LogGen.loggen()


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_mobile_from_csv(self, file_path="data/login_data.csv"):
        data = read_csv_data(file_path)

        assert data, "CSV is empty or file not found"

        mobile = str(data[0]["mobile"]).strip()

        assert mobile != "", "Mobile number is empty in CSV"

        logger.info("Mobile number fetched from CSV")
        return mobile

    def click_login(self):
        self.click_element(LoginLocators.LOGIN_BUTTON, "Login button")
        logger.info("Login button clicked")

    def enter_mobile_email(self, mobile=None):
        if mobile is None:
            mobile = self.get_mobile_from_csv()

        mobile = str(mobile).strip()

        assert mobile != "", "Mobile number should not be empty"

        mobile_input = WaitUtils.wait_for_element_visible(
            self.driver,
            LoginLocators.MOBILE_INPUT,
            timeout=180
        )

        assert mobile_input is not None, "Mobile input field not visible"

        self.driver.execute_script("arguments[0].focus();", mobile_input)
        self.driver.execute_script("arguments[0].value = '';", mobile_input)

        mobile_input.send_keys(mobile)

        assert mobile_input.get_attribute("value") == mobile, \
            "Mobile number was not entered correctly"

        logger.info("Mobile number entered")

    def click_continue(self):
        continue_button = WaitUtils.wait_for_element_clickable(
            self.driver,
            LoginLocators.CONTINUE_BUTTON,
            timeout=180
        )

        assert continue_button is not None, "Continue button not clickable"

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            continue_button
        )

        self.driver.execute_script("arguments[0].click();", continue_button)

        logger.info("Continue button clicked")

    def is_continue_button_disabled(self):
        continue_button = WaitUtils.wait_for_presence_of_element(
            self.driver,
            LoginLocators.CONTINUE_BUTTON,
            timeout=180
        )

        assert continue_button is not None, "Continue button not found"

        is_disabled = (
            continue_button.get_attribute("disabled") is not None
            or continue_button.get_attribute("aria-disabled") == "true"
            or not continue_button.is_enabled()
        )

        assert is_disabled, "Continue button is enabled for invalid mobile number"

        logger.info("Continue button is disabled for invalid mobile number")

        return is_disabled

    def enter_otp(self, otp):
        otp = str(otp).strip()

        assert otp != "", "OTP should not be empty"

        self.enter_text(LoginLocators.OTP_INPUT, otp, "OTP field")

        logger.info("OTP entered")

    def click_verify(self):
        verify_button = WaitUtils.wait_for_element_clickable(
            self.driver,
            LoginLocators.VERIFY_BUTTON,
            timeout=180
        )

        assert verify_button is not None, "Verify button not clickable"

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            verify_button
        )

        self.driver.execute_script("arguments[0].click();", verify_button)

        logger.info("Verify button clicked")

    def get_otp_error_message(self):
        try:
            message_element = WaitUtils.wait_for_element_visible(
                self.driver,
                LoginLocators.OTP_ERROR,
                timeout=200
            )

            assert message_element is not None, "OTP error message not visible"

            message = message_element.text.strip()

            assert message != "", "OTP error message is empty"

            logger.info(f"OTP error displayed: {message}")
            return message

        except Exception:
            logger.info("OTP error message not displayed")
            return None

    def verify_invalid_otp_error_displayed(self):
        error_message = self.get_otp_error_message()

        assert error_message is not None, "Invalid OTP error message not displayed"

        assert (
            "otp" in error_message.lower()
            or "invalid" in error_message.lower()
            or "valid" in error_message.lower()
        ), "Invalid OTP error text is not correct"

        logger.info("Invalid OTP error message verified successfully")