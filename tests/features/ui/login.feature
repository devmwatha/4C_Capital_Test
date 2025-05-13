Feature: SauceDemo Login
    As a user
    I want to login to SauceDemo
    So that I can access the products

    Scenario: Successful login with valid credentials
        Given I am on the login page
        When I login with username "standard_user" and password "secret_sauce"
        Then I should be redirected to the products page

    Scenario: Failed login with invalid credentials
        Given I am on the login page
        When I login with username "invalid_user" and password "wrong_password"
        Then I should see an error message "Epic sadface: Username and password do not match any user in this service"

    Scenario: Logout from application
        Given I am logged in with valid credentials
        When I logout from the application
        Then I should be redirected to the login page