from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.config_reader import ConfigReader


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 20)

    # ---------- LOCATORS ----------
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")
    MOBILE_INPUT = (By.XPATH, "//input[@placeholder='Enter Phone number/ Email Id']")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Continue']")
    OTP_INPUT = (By.XPATH, "//input[@type='text' or contains(@placeholder,'OTP')]")
    VERIFY_BUTTON = (By.XPATH, "//button[contains(text(),'Verify')]")

    OTP_ERROR = (
        By.XPATH,
        "//*[contains(text(),'OTP') or contains(text(),'invalid') or contains(text(),'valid')]"
    )

    # ---------- ACTION METHODS ----------

    def open_bigbasket(self):
        url = ConfigReader.get("base_url")
        self.open_url(url)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def enter_mobile_email(self, value):
        field = self.wait.until(EC.visibility_of_element_located(self.MOBILE_INPUT))
        field.clear()
        field.send_keys(value)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    def enter_otp(self, otp):
        field = self.wait.until(EC.visibility_of_element_located(self.OTP_INPUT))
        field.clear()
        field.send_keys(otp)

    def click_verify(self):

        verify_button = self.wait.until(
            EC.visibility_of_element_located(self.VERIFY_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            verify_button
        )

        self.wait.until(
            EC.element_to_be_clickable(self.VERIFY_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            verify_button
        )
    # ---------- NEGATIVE VALIDATION ----------
    def get_otp_error_message(self):
        try:
            msg = self.wait.until(
                EC.presence_of_element_located(self.OTP_ERROR)
            )
            return msg.text.strip()
        except:
            return None