from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def username_input(self):
        return self.wait.until(EC.visibility_of_element_located(
            (By.ID, "user-name")
        ))

    @property
    def password_input(self):
        return self.wait.until(EC.visibility_of_element_located(
            (By.ID, "password")
        ))

    @property
    def login_button(self):
        return self.wait.until(EC.visibility_of_element_located(
            (By.ID, "login-button")
        ))

    def load(self):
        self.driver.get("https://www.saucedemo.com/")
        return self

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        return ProductsPage(self.driver)

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))).text


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        return "inventory" in self.driver.current_url

    def add_to_cart(self, product_name):
        item_container = self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']")
        item_container.find_element(By.CLASS_NAME, "btn_inventory").click()
        return self

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        return CartPage(self.driver)

    def logout(self):
        # Open the menu
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "react-burger-menu-btn")
        )).click()

        # Wait for logout link and click it
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "logout_sidebar_link")
        )).click()

        # Return login page object
        return LoginPage(self.driver)



class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        return "cart" in self.driver.current_url

    def get_cart_items(self):
        return [item.text for item in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]

    def remove_item(self, product_name):
        self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='cart_item']//button").click()
        return self

    def is_cart_empty(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "cart_item")) == 0