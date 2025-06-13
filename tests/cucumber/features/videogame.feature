Feature: Video Game API
  Scenario: Get all video games
    When the client sends a GET request to "/api/videogame"
    Then the response status code should be 200
    And the response should be a list of video games

  Scenario: Get a video game by ID
    When the client sends a GET request to "/api/videogame/1"
    Then the response status code should be 200
    And the response should contain a video game with ID 1