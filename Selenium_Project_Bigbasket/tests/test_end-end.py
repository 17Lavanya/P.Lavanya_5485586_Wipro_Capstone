import time
import allure
import pytest

from pages.login_page import LoginPage
from pages.electronics_page import ElectronicsPage
from utils.csv_reader import read_csv_data
from utils.logger import LogGen


logger = LogGen.loggen()

# Read CSV once
data = read_csv_data("data/login_data.csv")
mobile_data = [(row["mobile"],) for row in data]


@allure.feature("Electronics Module")
@allure.story("Search Electronics Product")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("BigBasket Electronics Flow")

@pytest.mark.parametrize("mobile", mobile_data)
def test_bigbasket_electronics_flow(driver, mobile):

    mobile = mobile[0]

    login = LoginPage(driver)

    login.open_bigbasket()
    logger.info("BigBasket website opened")
    time.sleep(3)

    login.click_login()
    logger.info("Login button clicked")
    time.sleep(2)

    login.enter_mobile_email(mobile)
    logger.info("Mobile number entered")

    login.click_continue()
    logger.info("Continue button clicked")

    time.sleep(20)

    login.click_verify()
    logger.info("Login successful")

    # =========================
    # ELECTRONICS FLOW
    # =========================
    category = ElectronicsPage(driver)

    category.click_got_it()
    logger.info("Got It popup handled")
    time.sleep(2)

    category.click_shop_by_category()
    logger.info("Shop By Category opened")
    time.sleep(2)

    category.click_electronics()
    logger.info("Electronics category opened")
    time.sleep(3)

    category.click_audio_devices()
    logger.info("Audio devices opened")
    time.sleep(3)

    category.click_earbuds()
    logger.info("Earbuds section opened")
    time.sleep(3)

    category.add_first_earbud_two_times()
    logger.info("First earbud quantity increased")
    time.sleep(3)

    category.click_brands_filter()
    logger.info("Brand filter opened")
    time.sleep(2)

    category.select_boat_brand()
    logger.info("Boat brand selected")
    time.sleep(3)

    category.click_add_button()
    logger.info("Product added to basket")
    time.sleep(3)

    category.click_basket()
    logger.info("Basket opened")
    time.sleep(3)

    category.click_increment()
    logger.info("Product quantity incremented")
    time.sleep(2)

    category.click_checkout()
    logger.info("Checkout page opened")
    time.sleep(3)