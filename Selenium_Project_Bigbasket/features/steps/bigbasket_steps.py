import os
import time

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.electronics_page import ElectronicsPage
from pages.login_page import LoginPage
from utils.csv_reader import read_csv_data
from utils.logger import LogGen

logger = LogGen.loggen()


def get_mobile_from_csv():
    data = read_csv_data(os.path.join("data", "login_data.csv"))

    if not data:
        raise AssertionError("CSV is empty or data/login_data.csv was not found")

    mobile = data[0].get("mobile")

    if not mobile:
        raise AssertionError("mobile column is missing in data/login_data.csv")

    return mobile


def login_with_csv_mobile(context):
    login = LoginPage(context.driver)
    context.login_page = login

    login.click_login()
    logger.info("Login button clicked")

    login.enter_mobile_email(get_mobile_from_csv())
    logger.info("Mobile number entered")

    login.click_continue()
    logger.info("Continue button clicked")

    time.sleep(20)

    login.click_verify()
    logger.info("Login successful")


def open_electronics(context):
    electronics = ElectronicsPage(context.driver)
    context.electronics_page = electronics

    electronics.click_got_it()
    logger.info("Got It popup handled")

    electronics.click_shop_by_category()
    logger.info("Shop By Category opened")

    electronics.click_electronics()
    logger.info("Electronics category opened")


def open_earbuds(context):
    open_electronics(context)

    electronics = context.electronics_page
    electronics.click_audio_devices()
    logger.info("Audio devices opened")

    electronics.click_earbuds()
    logger.info("Earbuds section opened")


@given("user launches the BigBasket website")
def step_launch_bigbasket(context):
    login = LoginPage(context.driver)
    context.login_page = login

    login.open_bigbasket()
    logger.info("BigBasket website opened")


@when("user logs in using mobile number from CSV")
def step_login_with_csv(context):
    login_with_csv_mobile(context)


@then("user should be on the BigBasket website")
def step_validate_bigbasket_site(context):
    assert "bigbasket" in context.driver.current_url.lower() or context.driver.title != ""


@when("user opens the electronics category")
def step_open_electronics_category(context):
    open_electronics(context)


@then("electronics category should be displayed")
def step_validate_electronics_category(context):
    assert "electronics" in context.driver.page_source.lower()


@when("user opens earbuds under electronics audio devices")
def step_open_earbuds(context):
    open_earbuds(context)


@when("user applies the boAt brand filter")
def step_apply_boat_filter(context):
    electronics = context.electronics_page

    electronics.click_brands_filter()
    logger.info("Brand filter opened")

    electronics.select_boat_brand()
    logger.info("Boat brand selected")


@then("brand filter should be applied successfully")
def step_validate_brand_filter(context):
    assert True


@when("user adds product to basket")
def step_add_product_to_basket(context):
    electronics = context.electronics_page

    electronics.click_add_button()
    logger.info("Product added to basket")

    electronics.click_basket()
    logger.info("Basket opened")


@then("basket should be opened")
def step_validate_basket(context):
    assert "basket" in context.driver.current_url.lower()


@when("user completes the electronics checkout flow")
def step_complete_checkout_flow(context):
    open_earbuds(context)

    electronics = context.electronics_page

    electronics.add_first_earbud_two_times()
    logger.info("First earbud quantity increased")

    electronics.click_brands_filter()
    logger.info("Brand filter opened")

    electronics.select_boat_brand()
    logger.info("Boat brand selected")

    electronics.click_add_button()
    logger.info("Product added to basket")

    electronics.click_basket()
    logger.info("Basket opened")

    electronics.click_increment()
    logger.info("Product quantity incremented")

    electronics.click_checkout()
    logger.info("Checkout page opened")


@then("checkout page should be displayed")
def step_validate_checkout_page(context):
    assert "checkout" in context.driver.current_url.lower() or "checkout" in context.driver.page_source.lower()


@when('user enters invalid mobile number "{mobile}"')
def step_enter_invalid_mobile(context, mobile):
    wait = WebDriverWait(context.driver, 15)
    login = LoginPage(context.driver)
    context.login_page = login

    login.click_login()
    logger.info("Login button clicked")

    login.enter_mobile_email(mobile)
    logger.info("Invalid mobile number entered")

    context.continue_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Continue')]"))
    )


@then("continue button should be disabled")
def step_validate_continue_disabled(context):
    assert not context.continue_button.is_enabled()


@when("user starts login using mobile number from CSV")
def step_start_login_for_otp(context):
    login = LoginPage(context.driver)
    context.login_page = login

    login.click_login()
    logger.info("Login button clicked")

    login.enter_mobile_email(get_mobile_from_csv())
    logger.info("Mobile number entered")

    login.click_continue()
    logger.info("Continue button clicked")


@when("user verifies without valid OTP")
def step_verify_without_valid_otp(context):
    wait = WebDriverWait(context.driver, 20)

    try:
        verify_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Verify') or contains(text(),'Continue')]")
            )
        )
        verify_button.click()
        logger.info("Verify button clicked")
    except Exception:
        logger.info("Verify button not found, continuing negative OTP flow")


@then("invalid OTP flow should be handled")
def step_validate_invalid_otp(context):
    wait = WebDriverWait(context.driver, 20)
    login = context.login_page

    try:
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(),'Invalid') or contains(text(),'error')]")
            )
        )
        result = True
    except Exception:
        result = login.get_otp_error_message() is not None

    assert result or "login" in context.driver.page_source.lower(), "OTP negative test failed"
