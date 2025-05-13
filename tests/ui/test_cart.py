import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage

scenarios('../features/ui/cart.feature')

@pytest.fixture
def login_page(browser):
    return LoginPage(browser)

@given("I am logged in with valid credentials")
def logged_in(login_page):
    products_page = login_page.load().login("standard_user", "secret_sauce")
    return products_page

@when(parsers.parse('I add "{product}" to the cart'))
def add_to_cart(logged_in, product):
    logged_in.add_to_cart(product)

@then(parsers.parse('the cart should contain "{product}"'))
def verify_cart_content(logged_in, product):
    cart_page = logged_in.go_to_cart()
    assert product in cart_page.get_cart_items()

@given(parsers.parse('I have "{product}" in my cart'))
def product_in_cart(logged_in, product):
    logged_in.add_to_cart(product)
    return logged_in

@when(parsers.parse('I remove "{product}" from the cart'))
def remove_from_cart(product_in_cart, product):
    cart_page = product_in_cart.go_to_cart()
    cart_page.remove_item(product)

@then("the cart should be empty")
def verify_empty_cart(product_in_cart):
    cart_page = product_in_cart.go_to_cart()
    assert cart_page.is_cart_empty()