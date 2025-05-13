import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def browser():
    """Fixture for Edge browser setup and teardown"""
    edge_options = Options()
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    edge_options.add_argument("--window-size=1920,1080")

    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=edge_options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.fixture
def context():
    """Shared context for BDD tests"""
    return {}

@pytest.fixture
def logged_in(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")
    return login_page  # or return some logged-in state/page object