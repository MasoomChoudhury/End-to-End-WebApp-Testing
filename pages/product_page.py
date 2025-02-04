from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_to_cart(self):
        self.click_element(ProductPageLocators.ADD_TO_CART_BUTTON)
