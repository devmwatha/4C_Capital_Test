import pytest
from pytest_bdd import scenarios, given, when, then, parsers

# Load the feature file
scenarios('../features/ui/login.feature')


# Fixtures and helper functions
@pytest.fixture
def browser():
    # In a real implementation, this would initialize a browser instance
    return {"current_page": "login"}


@pytest.fixture
def user_credentials():
    return {"username": "", "password": ""}


# Step definitions
@given("I am on the login page")
def on_login_page(browser):
    browser["current_page"] = "login"
    assert browser["current_page"] == "login"


@when(parsers.parse('I login with username "{username}" and password "{password}"'))
def login_with_credentials(browser, user_credentials, username, password):
    user_credentials["username"] = username
    user_credentials["password"] = password

    # Mock authentication logic
    if username == "standard_user" and password == "secret_sauce":
        browser["current_page"] = "products"
        browser["error_message"] = None
    else:
        browser["current_page"] = "login"
        browser["error_message"] = "Epic sadface: Username and password do not match any user in this service"


@then("I should be redirected to the products page")
def verify_products_page(browser):
    assert browser["current_page"] == "products"


@then(parsers.parse('I should see an error message "{error_message}"'))
def verify_error_message(browser, error_message):
    assert browser["error_message"] == error_message


@given("I am logged in with valid credentials")
def logged_in_with_valid_credentials(browser, user_credentials):
    browser["current_page"] = "login"
    login_with_credentials(browser, user_credentials, "standard_user", "secret_sauce")
    assert browser["current_page"] == "products"


@when("I logout from the application")
def logout_from_application(browser):
    browser["current_page"] = "login"


@then("I should be redirected to the login page")
def verify_login_page(browser):
    assert browser["current_page"] == "login"
