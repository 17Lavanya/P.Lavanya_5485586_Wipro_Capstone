from selenium.webdriver.common.by import By


class LoginLocators:

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Login')]"
    )

    MOBILE_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter Phone number/ Email Id']"
    )
    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Continue']"
    )

    ENABLED_CONTINUE_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Continue' and not(@disabled)]"
    )
    OTP_INPUT = (
        By.XPATH,
        "//input[@type='text' or contains(@placeholder,'OTP')]"
    )

    VERIFY_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Verify')]"
    )

    OTP_ERROR = (
        By.XPATH,
        "//*[contains(text(),'OTP') or contains(text(),'invalid') or contains(text(),'valid')]"
    )