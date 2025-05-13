import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage

scenarios('../features/ui/login.feature')

@pytest.fixture
def login_page(browser):
    return LoginPage(browser)

@given("I am on the login page")
def load_login_page(login_page):
    login_page.load()

@when(parsers.parse('I login with username "{username}" and password "{password}"'))
def login(login_page, username, password):
    login_page.login(username, password)

@then("I should be redirected to the products page")
def verify_products_page(browser):
    assert "inventory" in browser.current_url

@then(parsers.parse('I should see an error message "{message}"'))
def verify_error_message(browser, message):
    assert message in browser.page_source

@given("I am logged in with valid credentials")
def logged_in(login_page):
    login_page.load().login("standard_user", "secret_sauce")

@when("I logout from the application")
def logout(login_page):
    login_page.logout()

@then("I should be redirected to the login page")
def verify_login_page(browser):
    assert "login" in browser.current_url.lower()