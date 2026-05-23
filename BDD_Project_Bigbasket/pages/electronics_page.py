from locators.electronics_locators import ElectronicsLocators
from pages.base_page import BasePage
from utils.logger import LogGen
from utils.waits import WaitUtils

import time


logger = LogGen.loggen()


class ElectronicsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def scroll_and_click(self, locator):

        element = WaitUtils.wait_for_presence_of_element(
            self.driver,
            locator,
            timeout=180
        )

        assert element is not None, "Element was not found on the page"

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        logger.info("Scrolled and clicked successfully")

    def click_got_it(self):
        self.safe_click(ElectronicsLocators.GOT_IT_BUTTON)
        logger.info("Got It popup handled")

    def click_shop_by_category(self):
        self.scroll_and_click(ElectronicsLocators.SHOP_CATEGORY)
        logger.info("Shop By Category opened")

    def click_electronics(self):
        self.scroll_and_click(ElectronicsLocators.ELECTRONICS_CATEGORY)
        logger.info("Electronics category opened")

    def click_audio_devices(self, subcategory="Audio Devices"):
        self.scroll_and_click(
            ElectronicsLocators.subcategory_locator(subcategory)
        )
        logger.info(f"{subcategory} category opened")

    def click_earbuds(self, product_type="Earbuds"):
        self.scroll_and_click(
            ElectronicsLocators.product_type_locator(product_type)
        )
        logger.info(f"{product_type} page opened successfully")

    def click_brands_filter(self):
        self.driver.execute_script("window.scrollBy(0,400);")
        time.sleep(2)

        self.scroll_and_click(ElectronicsLocators.BRANDS_FILTER)
        logger.info("Brands filter opened")

    def select_boat_brand(self, brand="boAt"):
        time.sleep(2)

        self.scroll_and_click(
            ElectronicsLocators.brand_locator(brand)
        )

        logger.info(f"{brand} brand selected")

        time.sleep(4)

    def add_first_earbud_two_times(self):

        self.driver.execute_script(
            "window.scrollBy(0,700);"
        )

        time.sleep(4)

        add_buttons = self.driver.find_elements(
            *ElectronicsLocators.ADD_BUTTON
        )

        assert len(add_buttons) > 0, "No Add buttons found"

        add_clicked = False

        for button in add_buttons:

            if button.is_displayed() and button.is_enabled():
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    button
                )

                time.sleep(2)

                self.driver.execute_script(
                    "arguments[0].click();",
                    button
                )

                add_clicked = True

                logger.info("First ADD button clicked")

                break

        assert add_clicked, "First earbud was not added"

        time.sleep(4)

        increment_buttons = self.driver.find_elements(
            *ElectronicsLocators.INCREMENT_BUTTON
        )

        if len(increment_buttons) > 0:

            for button in increment_buttons:

                if button.is_displayed() and button.is_enabled():
                    self.driver.execute_script(
                        "arguments[0].click();",
                        button
                    )

                    logger.info("Increment button clicked")

                    break

        else:
            logger.info("Increment button not visible, product already added")

        time.sleep(3)

    def click_add_button(self):

        self.driver.execute_script(
            "window.scrollBy(0,700);"
        )

        time.sleep(3)

        self.scroll_and_click(
            ElectronicsLocators.ADD_BUTTON
        )

        logger.info("Product added to basket")

    def click_basket(self):
        self.driver.get("https://www.bigbasket.com/basket/")
        time.sleep(5)

        assert "basket" in self.driver.current_url, "Basket page did not open"
        logger.info("Basket opened successfully")

    def click_increment(self):
        from selenium.webdriver.common.by import By

        time.sleep(5)

        increment_button = self.driver.find_element(
            By.XPATH,
            "(//button[@id='increment'])[1]"
        )

        assert increment_button is not None, "Basket increment button not found"

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            increment_button
        )

        time.sleep(2)

        assert increment_button.is_displayed(), "Basket increment button is not visible"

        self.driver.execute_script(
            "arguments[0].click();",
            increment_button
        )

        time.sleep(5)

        logger.info("Product quantity incremented")

    def click_checkout(self):
        time.sleep(5)

        checkout_button = self.driver.find_element(
            *ElectronicsLocators.CHECKOUT_BUTTON
        )

        assert checkout_button is not None, "Proceed to Checkout button not found"

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            checkout_button
        )

        time.sleep(3)

        assert checkout_button.is_displayed(), "Proceed to Checkout button is not visible"

        self.driver.execute_script(
            "arguments[0].click();",
            checkout_button
        )

        logger.info("Proceed to Checkout clicked")

        time.sleep(10)

        assert (
            "checkout" in self.driver.current_url
            or "co" in self.driver.current_url
            or "payment" in self.driver.current_url
        ), "Checkout page did not open successfully"

        logger.info("Checkout page opened successfully")