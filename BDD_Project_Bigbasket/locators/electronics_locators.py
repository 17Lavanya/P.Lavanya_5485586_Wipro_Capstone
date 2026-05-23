from selenium.webdriver.common.by import By


class ElectronicsLocators:

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
        "//a[contains(@href,'/cl/electronics')]"
    )

    AUDIO_DEVICES_CATEGORY = (
        By.XPATH,
        "//a[contains(@href,'audio-devices')]"
    )

    EARBUDS_CATEGORY = (
        By.XPATH,
        "//a[contains(@href,'earbuds')]"
    )

    BRANDS_FILTER = (
        By.XPATH,
        "//span[contains(text(),'Brands')]"
    )

    BOAT_BRAND = (
        By.XPATH,
        "//label[contains(.,'boAt')]"
    )

    ADD_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Add')]"
    )

    INCREMENT_BUTTON = (
        By.XPATH,
        "(//button[@id='increment'])[1]"
    )

    CHECKOUT_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Proceed to Checkout')]"
    )

    @staticmethod
    def subcategory_locator(subcategory):
        return (
            By.XPATH,
            "//a[contains(@href,'audio-devices')]"
        )

    @staticmethod
    def product_type_locator(product_type):
        return (
            By.XPATH,
            "//a[contains(@href,'earbuds')]"
        )

    @staticmethod
    def brand_locator(brand):

        return (
            By.XPATH,
            f"//label[contains(.,'{brand}')]"
        )