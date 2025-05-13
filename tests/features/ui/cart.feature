Feature: Shopping Cart Management
    As a logged in user
    I want to manage my shopping cart
    So that I can prepare items for purchase

    Scenario: Add product to cart
        Given I am logged in with valid credentials
        When I add "Sauce Labs Backpack" to the cart
        Then the cart should contain "Sauce Labs Backpack"

    Scenario: Remove product from cart
        Given I have "Sauce Labs Backpack" in my cart
        When I remove "Sauce Labs Backpack" from the cart
        Then the cart should be empty