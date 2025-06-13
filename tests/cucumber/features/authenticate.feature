Feature: Authentication
  Scenario: Successful login
    Given the API credentials are "admin" and "admin"
    When the client sends a POST request to "/api/authenticate"
    Then the response status code should be 200
    And the response should contain a token