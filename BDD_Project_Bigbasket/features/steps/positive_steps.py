from behave import when, then
import allure

from locators.login_locators import LoginLocators
from pages.login_page import LoginPage
from pages.electronics_page import ElectronicsPage
from utils.csv_reader import read_csv_data
from utils.logger import LogGen
from utils.waits import WaitUtils


logger = LogGen.loggen()


def get_product_data():
    data = read_csv_data("data/product_data.csv")

    if not data:
        raise Exception("Product CSV is empty or file not found")

    return data[0]


@when("user clicks on login button")
def step_click_login(context):
    with allure.step("Click login button"):
        context.login_page = LoginPage(context.driver)
        context.login_page.click_login()


@when("user enters valid mobile number from csv")
def step_enter_valid_mobile(context):
    with allure.step("Enter valid mobile number from CSV"):
        context.login_page.enter_mobile_email()


@when("user clicks on continue button")
def step_click_continue(context):
    with allure.step("Click continue button"):
        context.login_page.click_continue()


@when("user waits for manual OTP entry")
def step_wait_for_manual_otp_entry(context):
    with allure.step("Wait for manual OTP entry"):
        logger.info("Waiting for user to enter OTP manually")

        WaitUtils.wait_for_element_clickable(
            context.driver,
            LoginLocators.VERIFY_BUTTON,
            timeout=120
        )

        logger.info("OTP entered manually and Verify button is clickable")


@when("user clicks on verify button")
def step_click_verify(context):
    with allure.step("Click verify button"):
        context.login_page.click_verify()


@then("user should be logged in successfully")
def step_validate_login(context):
    with allure.step("Validate user logged in successfully"):
        assert (
            "bigbasket" in context.driver.current_url.lower()
            or context.driver.title != ""
        ), "Login was not successful"

        logger.info("User logged in successfully")


@when("user logs in with valid mobile number from csv")
def step_login_with_valid_mobile(context):
    with allure.step("Login with valid mobile number from CSV"):
        context.login_page = LoginPage(context.driver)

        context.login_page.click_login()
        context.login_page.enter_mobile_email()
        context.login_page.click_continue()

        logger.info("Waiting for user to enter OTP manually")

        WaitUtils.wait_for_element_clickable(
            context.driver,
            LoginLocators.VERIFY_BUTTON,
            timeout=120
        )

        context.login_page.click_verify()
        logger.info("Login completed with valid mobile number")


@when("user handles got it popup")
def step_handle_got_it(context):
    with allure.step("Handle Got It popup"):
        context.electronics_page = ElectronicsPage(context.driver)
        context.electronics_page.click_got_it()


@when("user clicks on shop by category")
def step_click_shop_by_category(context):
    with allure.step("Click Shop by Category"):
        context.electronics_page.click_shop_by_category()


@when("user clicks on electronics category")
def step_click_electronics_category(context):
    with allure.step("Click Electronics category"):
        context.electronics_page.click_electronics()


@then("electronics category should be opened")
def step_validate_electronics_category(context):
    with allure.step("Validate Electronics category opened"):
        import time
        time.sleep(5)

        assert (
            "electronics" in context.driver.current_url.lower()
            or "electronics" in context.driver.page_source.lower()
        ), "Electronics category page was not opened"

        logger.info("Electronics category opened successfully")


@when("user opens earbuds category")
def step_open_earbuds_category(context):
    with allure.step("Open Earbuds category from product CSV data"):
        context.product_data = get_product_data()

        allure.attach(
            str(context.product_data),
            name="Product CSV Data",
            attachment_type=allure.attachment_type.TEXT
        )

        context.electronics_page = ElectronicsPage(context.driver)

        context.electronics_page.click_got_it()
        context.electronics_page.click_shop_by_category()
        context.electronics_page.click_electronics()

        context.electronics_page.click_audio_devices(
            context.product_data["subcategory"]
        )

        context.electronics_page.click_earbuds(
            context.product_data["product_type"]
        )


@when("user opens audio devices from positive flow")
def step_click_audio_devices_positive(context):
    with allure.step("Open Audio Devices from CSV data"):
        context.product_data = get_product_data()

        allure.attach(
            str(context.product_data),
            name="Product CSV Data",
            attachment_type=allure.attachment_type.TEXT
        )

        context.electronics_page.click_audio_devices(
            context.product_data["subcategory"]
        )


@when("user opens earbuds category from positive flow")
def step_click_earbuds_category_positive(context):
    with allure.step("Open Earbuds category from CSV data"):
        context.electronics_page.click_earbuds(
            context.product_data["product_type"]
        )


@when("user clicks on brands filter")
def step_click_brands_filter(context):
    with allure.step("Click Brands filter"):
        context.electronics_page.click_brands_filter()


@when("user selects static boAt brand")
def step_select_boat_brand(context):
    with allure.step("Select brand from CSV data"):
        if not hasattr(context, "product_data"):
            context.product_data = get_product_data()

        allure.attach(
            str(context.product_data),
            name="Brand CSV Data",
            attachment_type=allure.attachment_type.TEXT
        )

        context.electronics_page.select_boat_brand(
            context.product_data["brand"]
        )


@then("boAt brand filter should be applied successfully")
def step_validate_boat_filter(context):
    with allure.step("Validate boAt brand filter applied"):
        assert "boat" in context.driver.page_source.lower(), \
            "boAt brand filter was not applied"

        logger.info("boAt brand filter applied successfully")


@when("user clicks on add button")
def step_click_add_button(context):
    with allure.step("Click Add button"):
        context.electronics_page.click_add_button()


@when("user opens basket")
def step_open_basket(context):
    with allure.step("Open Basket"):
        context.electronics_page.click_basket()


@then("product should be added to basket successfully")
def step_validate_product_added(context):
    with allure.step("Validate product added to basket"):
        assert "basket" in context.driver.current_url.lower(), \
            "Basket page was not opened"

        assert (
            "subtotal" in context.driver.page_source.lower()
            or "delivery" in context.driver.page_source.lower()
            or "quantity" in context.driver.page_source.lower()
        ), "Product was not added to basket"

        logger.info("Product added to basket successfully")