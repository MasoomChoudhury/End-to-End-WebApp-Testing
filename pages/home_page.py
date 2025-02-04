from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")
    PRODUCT_ITEM = (By.CSS_SELECTOR, ".product-item")
    CART_LINK = (By.CSS_SELECTOR, "#cart-total")

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def search_product(self, product_name):
        self.type_text(HomePageLocators.SEARCH_INPUT, product_name)
        self.click_element(HomePageLocators.SEARCH_BUTTON)

    def select_product(self):
        self.click_element(HomePageLocators.PRODUCT_ITEM)

    def go_to_cart(self):
        self.click_element(HomePageLocators.CART_LINK)
