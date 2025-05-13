Feature: Rest Countries API
    As an API consumer
    I want to interact with the Rest Countries API
    So that I can get information about countries

    Scenario: Get countries by valid currency code
        When I request countries with currency "KES"
        Then the response status code should be 200
        And the response should contain at least one country

    Scenario: Get countries by invalid currency code
        When I request countries with currency "XXX"
        Then the response status code should be 404
        And the response should contain message "Not Found"

    Scenario: Verify response structure for valid currency
        When I request countries with currency "USD"
        Then the response should match the expected schema