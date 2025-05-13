import pytest
from pytest_bdd import scenarios, given, when, then, parsers

# Load the feature file
scenarios('../features/ui/cart.feature')

# Shared fixture for the shopping cart
@pytest.fixture
def shopping_cart():
    return []

# Step definitions for Add product to cart scenario
@given("I am logged in with valid credentials")
def logged_in_user():
    # In a real implementation, this would actually log in the user
    return {"username": "test_user", "logged_in": True}

@when('I add "Sauce Labs Backpack" to the cart')
def add_product_to_cart(shopping_cart):
    shopping_cart.append("Sauce Labs Backpack")

@then('the cart should contain "Sauce Labs Backpack"')
def cart_should_contain_product(shopping_cart):
    assert "Sauce Labs Backpack" in shopping_cart

# Step definitions for Remove product from cart scenario
@given('I have "Sauce Labs Backpack" in my cart')
def product_in_cart(shopping_cart):
    shopping_cart.append("Sauce Labs Backpack")
    assert "Sauce Labs Backpack" in shopping_cart

@when('I remove "Sauce Labs Backpack" from the cart')
def remove_product_from_cart(shopping_cart):
    shopping_cart.remove("Sauce Labs Backpack")

@then("the cart should be empty")
def cart_should_be_empty(shopping_cart):
    assert len(shopping_cart) == 0
