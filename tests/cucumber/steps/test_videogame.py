import requests
import pytest
from pytest_bdd import scenarios, when, then

scenarios('../features/videogame.feature')

@when('the client sends a GET request to "/api/videogame"')
def get_all_games(base_url):
    response = requests.get(f"{base_url}/api/videogame")
    pytest.shared_response = response

@when('the client sends a GET request to "/api/videogame/1"')
def get_game_by_id(base_url):
    response = requests.get(f"{base_url}/api/videogame/1")
    pytest.shared_response = response

@then('the response status code should be 200')
def check_status():
    assert pytest.shared_response.status_code == 200

@then('the response should be a list of video games')
def check_list():
    assert isinstance(pytest.shared_response.json(), list)

@then('the response should contain a video game with ID 1')
def check_game_id():
    game = pytest.shared_response.json()
    assert game["id"] == 1