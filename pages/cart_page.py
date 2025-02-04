from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPageLocators:
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn-primary")

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def proceed_to_checkout(self):
        self.click_element(CartPageLocators.CHECKOUT_BUTTON)
