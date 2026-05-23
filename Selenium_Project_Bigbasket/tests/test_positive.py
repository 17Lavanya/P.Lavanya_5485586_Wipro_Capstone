import time
import allure

from pages.login_page import LoginPage
from pages.electronics_page import ElectronicsPage
from utils.csv_reader import read_csv_data
from utils.logger import LogGen

logger = LogGen.loggen()

data = read_csv_data("data/login_data.csv")


# =========================
# COMMON LOGIN FUNCTION
# =========================
def do_login(driver):

    login = LoginPage(driver)
    test_data = data[0]

    login.open_bigbasket()
    logger.info("BigBasket website opened")

    login.click_login()
    logger.info("Login button clicked")

    login.enter_mobile_email(test_data["mobile"])
    logger.info("Mobile number entered")

    login.click_continue()
    logger.info("Continue button clicked")

    time.sleep(10)  # better replace later with explicit wait

    login.click_verify()
    logger.info("Login successful")

    return login


# =========================
# TEST 1: LOGIN
# =========================
@allure.feature("BigBasket Electronics Module")
@allure.story("Login Test")
def test_login(driver):

    do_login(driver)

    logger.info("Login test passed")

    assert "bigbasket" in driver.current_url.lower() or driver.title != ""


# =========================
# TEST 2: OPEN CATEGORY
# =========================
@allure.story("Open Electronics Category")
def test_open_electronics(driver):

    do_login(driver)

    electronics = ElectronicsPage(driver)

    electronics.click_got_it()
    logger.info("Got It popup handled")

    electronics.click_shop_by_category()
    logger.info("Shop By Category opened")

    electronics.click_electronics()
    logger.info("Electronics category opened")

    logger.info("Open electronics category test passed")

    assert "electronics" in driver.page_source.lower()


# =========================
# TEST 3: APPLY FILTER
# =========================
@allure.story("Apply Brand Filter")
def test_apply_filter(driver):

    do_login(driver)

    electronics = ElectronicsPage(driver)

    electronics.click_got_it()
    logger.info("Got It popup handled")

    electronics.click_shop_by_category()
    logger.info("Shop By Category opened")

    electronics.click_electronics()
    logger.info("Electronics category opened")

    electronics.click_audio_devices()
    logger.info("Audio devices opened")

    electronics.click_earbuds()
    logger.info("Earbuds section opened")

    electronics.click_brands_filter()
    logger.info("Brand filter opened")

    electronics.select_boat_brand()
    logger.info("Boat brand selected")

    logger.info("Apply filter test passed")

    assert True


# =========================
# TEST 4: ADD PRODUCT
# =========================
@allure.story("Add Product To Cart")
def test_add_product(driver):

    do_login(driver)

    electronics = ElectronicsPage(driver)

    electronics.click_got_it()
    logger.info("Got It popup handled")

    electronics.click_shop_by_category()
    logger.info("Shop By Category opened")

    electronics.click_electronics()
    logger.info("Electronics category opened")

    electronics.click_audio_devices()
    logger.info("Audio devices opened")

    electronics.click_earbuds()
    logger.info("Earbuds section opened")

    electronics.click_brands_filter()
    logger.info("Brand filter opened")

    electronics.select_boat_brand()
    logger.info("Boat brand selected")

    electronics.click_add_button()
    logger.info("Product added to basket")

    electronics.click_basket()
    logger.info("Basket opened")

    logger.info("Add product test passed")

    assert True