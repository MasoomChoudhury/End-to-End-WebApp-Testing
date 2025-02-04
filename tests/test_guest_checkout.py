import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_guest_checkout(driver, config):
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    home_page.search_product("dress")
    home_page.select_product()
    product_page.add_to_cart()
    home_page.go_to_cart()
    cart_page.proceed_to_checkout()
    checkout_page.enter_guest_details()
    checkout_page.enter_shipping_address()
    checkout_page.select_shipping_method()
    checkout_page.select_payment_method()
    checkout_page.place_order()

    assert "Your order has been placed" in checkout_page.get_order_confirmation_message()
