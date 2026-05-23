from behave import when, then
import allure

from utils.csv_reader import read_csv_data
from utils.logger import LogGen


logger = LogGen.loggen()


def get_product_data():

    data = read_csv_data(
        "data/product_data.csv"
    )

    if not data:
        raise Exception(
            "Product CSV is empty or file not found"
        )

    return data[0]


@when("user clicks on audio devices")
def step_click_audio_devices(context):

    with allure.step("Read subcategory from CSV and open Audio Devices"):
        context.product_data = get_product_data()

        allure.attach(
            str(context.product_data),
            name="Product CSV Data",
            attachment_type=allure.attachment_type.TEXT
        )

        logger.info(
            f"Subcategory from CSV : "
            f"{context.product_data['subcategory']}"
        )

        context.electronics_page.click_audio_devices(
            context.product_data["subcategory"]
        )


@when("user clicks on earbuds category")
def step_click_earbuds_category(context):

    with allure.step("Read product type from CSV and open Earbuds category"):
        logger.info(
            f"Product type from CSV : "
            f"{context.product_data['product_type']}"
        )

        context.electronics_page.click_earbuds(
            context.product_data["product_type"]
        )


@when("user adds first earbud two times")
def step_add_first_earbud_two_times(context):

    with allure.step("Add first earbud and increase quantity"):
        context.electronics_page.add_first_earbud_two_times()


@when("user selects boAt brand")
def step_select_boat_brand(context):

    with allure.step("Select brand from CSV"):
        logger.info(
            f"Brand from CSV : "
            f"{context.product_data['brand']}"
        )

        context.electronics_page.select_boat_brand(
            context.product_data["brand"]
        )


@when("user increments product quantity")
def step_increment_product_quantity(context):

    with allure.step("Increment product quantity in basket"):
        context.electronics_page.click_increment()


@when("user clicks on checkout button")
def step_click_checkout_button(context):

    with allure.step("Click checkout button"):
        context.electronics_page.click_checkout()


@then("checkout page should be opened")
def step_validate_checkout_page(context):

    with allure.step("Validate checkout page opened"):
        assert (
            "checkout" in context.driver.current_url.lower()
            or "checkout" in context.driver.page_source.lower()
        )

        logger.info(
            "Checkout page opened successfully"
        )