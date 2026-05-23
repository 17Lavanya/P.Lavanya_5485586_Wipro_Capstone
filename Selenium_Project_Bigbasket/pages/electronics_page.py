import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utils.logger import LogGen
from pages.base_page import BasePage


class ElectronicsPage(BasePage):

    GOT_IT_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Got it')]"
    )

    SHOP_CATEGORY = (
        By.XPATH,
        "(//button[contains(.,'Category')])[2]"
    )

    ELECTRONICS_CATEGORY = (
        By.XPATH,
        "//a[@href='/cl/electronics/?nc=nb']"
    )

    AUDIO_DEVICES_CATEGORY = (
        By.XPATH,
        "//a[@href='/pc/electronics/audio-devices/?nc=nb']"
    )

    EARBUDS_CATEGORY = (
        By.XPATH,
        "//a[@href='/pc/electronics/audio-devices/earbuds/?nc=nb']"
    )

    # Brands Filter
    BRANDS_FILTER = (
        By.XPATH,
        "//span[contains(text(),'Brands')]"
    )

    # Boat Checkbox
    BOAT_BRAND = (
        By.XPATH,
        "//label[contains(.,'boAt')]"
    )

    # Add Button
    ADD_BUTTON = (
        By.XPATH,
        "(//button[contains(text(),'Add')])[2]"
    )

    # Increment Button
    INCREMENT_BUTTON = (
        By.XPATH,
        "//button[@id='increment']"
    )

    # Proceed Checkout
    CHECKOUT_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Proceed to Checkout')]"
    )

    def __init__(self, driver):
        super().__init__(driver)

    # Common Scroll And Click Method
    def scroll_and_click(self, locator):

        element = self.driver.find_element(*locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        time.sleep(2)

    # Click Got It
    #@allure.step("Click Got It Popup")
    def click_got_it(self):

        self.safe_click(self.GOT_IT_BUTTON)

    # Shop By Category
    #@allure.step("Click Shop By Category")
    def click_shop_by_category(self):

        self.scroll_and_click(
            self.SHOP_CATEGORY
        )

    # Electronics
    #@allure.step("Open Electronics Category")
    def click_electronics(self):

        self.scroll_and_click(
            self.ELECTRONICS_CATEGORY
        )

        time.sleep(2)

        # Close Menu
        ActionChains(self.driver).send_keys(
            Keys.ESCAPE
        ).perform()

        time.sleep(2)

        #print("Electronics page opened")

    # Audio Devices
    #@allure.step("Open Audio Devices")
    def click_audio_devices(self):

        self.scroll_and_click(
            self.AUDIO_DEVICES_CATEGORY
        )

    # Earbuds
    #@allure.step("Open Earbuds")
    def click_earbuds(self):

        self.scroll_and_click(
            self.EARBUDS_CATEGORY
        )

    # Add First Earbud Two Times
    #@allure.step("Add First Earbud Two Times")
    def add_first_earbud_two_times(self):

        self.scroll_and_click(
            self.ADD_BUTTON
        )

        #print("First click completed")

        time.sleep(3)

        self.scroll_and_click(
            self.ADD_BUTTON
        )

        #print("Second click completed")

    # Brands Filter
    #@allure.step("Click Brands Filter")
    def click_brands_filter(self):

        self.scroll_and_click(
            self.BRANDS_FILTER
        )

    # Select boAt Brand
    #@allure.step("Select boAt Brand")
    def select_boat_brand(self):

        self.scroll_and_click(
            self.BOAT_BRAND
        )

    # Add Product
    #@allure.step("Add Product To Cart")
    def click_add_button(self):

        self.scroll_and_click(
            self.ADD_BUTTON
        )

        #print("Product added successfully")

    # Open Basket
    #@allure.step("Open Basket")
    def click_basket(self):

        time.sleep(5)

        self.driver.get(
            "https://www.bigbasket.com/basket/"
        )

        #print("Basket opened successfully")

    # Increase Quantity
    #@allure.step("Increase Product Quantity")
    def click_increment(self):

        self.scroll_and_click(
            self.INCREMENT_BUTTON
        )

    # Proceed Checkout
    #@allure.step("Proceed To Checkout")
    def click_checkout(self):

        self.scroll_and_click(
            self.CHECKOUT_BUTTON
        )