from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPageLocators:
    GUEST_CHECKOUT_RADIO = (By.CSS_SELECTOR, "input[value='guest']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#button-account")
    FIRSTNAME_INPUT = (By.ID, "input-payment-firstname")
    LASTNAME_INPUT = (By.ID, "input-payment-lastname")
    EMAIL_INPUT = (By.ID, "input-payment-email")
    TELEPHONE_INPUT = (By.ID, "input-payment-telephone")
    PASSWORD_INPUT = (By.ID, "input-payment-password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "input-payment-confirm")
    COMPANY_INPUT = (By.ID, "input-payment-company")
    ADDRESS_1_INPUT = (By.ID, "input-payment-address-1")
    CITY_INPUT = (By.ID, "input-payment-city")
    POSTCODE_INPUT = (By.ID, "input-payment-postcode")
    COUNTRY_SELECT = (By.ID, "input-payment-country")
    REGION_SELECT = (By.ID, "input-payment-zone")
    GUEST_CONTINUE_BUTTON = (By.CSS_SELECTOR, "#button-guest")
    SHIPPING_FIRSTNAME_INPUT = (By.ID, "input-shipping-firstname")
    SHIPPING_LASTNAME_INPUT = (By.ID, "input-shipping-lastname")
    SHIPPING_COMPANY_INPUT = (By.ID, "input-shipping-company")
    SHIPPING_ADDRESS_1_INPUT = (By.ID, "input-shipping-address-1")
    SHIPPING_CITY_INPUT = (By.ID, "input-shipping-city")
    SHIPPING_POSTCODE_INPUT = (By.ID, "input-shipping-postcode")
    SHIPPING_COUNTRY_SELECT = (By.ID, "input-shipping-country")
    SHIPPING_REGION_SELECT = (By.ID, "input-shipping-zone")
    SHIPPING_GUEST_CONTINUE_BUTTON = (By.CSS_SELECTOR, "#button-guest-shipping")
    SHIPPING_METHOD_CONTINUE_BUTTON = (By.CSS_SELECTOR, "#button-shipping-method")
    PAYMENT_METHOD_CHECKBOX = (By.CSS_SELECTOR, "input[name='agree']")
    PAYMENT_METHOD_CONTINUE_BUTTON = (By.CSS_SELECTOR, "#button-payment-method")
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, "#button-confirm")
    ORDER_CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, "#content h1")


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_guest_details(self):
        self.click_element(CheckoutPageLocators.GUEST_CHECKOUT_RADIO)
        self.click_element(CheckoutPageLocators.CONTINUE_BUTTON)
        self.type_text(CheckoutPageLocators.FIRSTNAME_INPUT, "Guest")
        self.type_text(CheckoutPageLocators.LASTNAME_INPUT, "User")
        self.type_text(CheckoutPageLocators.EMAIL_INPUT, "guest@example.com")
        self.type_text(CheckoutPageLocators.TELEPHONE_INPUT, "1234567890")
        self.click_element(CheckoutPageLocators.GUEST_CONTINUE_BUTTON)

    def enter_shipping_address(self):
        self.type_text(CheckoutPageLocators.SHIPPING_FIRSTNAME_INPUT, "Guest")
        self.type_text(CheckoutPageLocators.SHIPPING_LASTNAME_INPUT, "User")
        self.type_text(CheckoutPageLocators.SHIPPING_COMPANY_INPUT, "Company")
        self.type_text(CheckoutPageLocators.SHIPPING_ADDRESS_1_INPUT, "Address 1")
        self.type_text(CheckoutPageLocators.SHIPPING_CITY_INPUT, "City")
        self.type_text(CheckoutPageLocators.SHIPPING_POSTCODE_INPUT, "12345")
        # Assuming default country and region are acceptable for now
        self.click_element(CheckoutPageLocators.SHIPPING_GUEST_CONTINUE_BUTTON)

    def select_shipping_method(self):
        self.click_element(CheckoutPageLocators.SHIPPING_METHOD_CONTINUE_BUTTON)

    def select_payment_method(self):
        self.click_element(CheckoutPageLocators.PAYMENT_METHOD_CHECKBOX)
        self.click_element(CheckoutPageLocators.PAYMENT_METHOD_CONTINUE_BUTTON)

    def place_order(self):
        self.click_element(CheckoutPageLocators.CONFIRM_ORDER_BUTTON)

    def get_order_confirmation_message(self):
        return self.get_text(CheckoutPageLocators.ORDER_CONFIRMATION_MESSAGE)
