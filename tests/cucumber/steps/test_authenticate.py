import requests
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

# Load the feature file
scenarios('../features/authenticate.feature')

# Shared response placeholder
shared = {}

@given(parsers.cfparse('the API credentials are "{username}" and "{password}"'), target_fixture="credentials")
def credentials(username, password):
    return {"username": username, "password": password}

@when('the client sends a POST request to "/api/authenticate"')
def post_authenticate(base_url, credentials):
    response = requests.post(f"{base_url}/api/authenticate", json=credentials)
    shared["response"] = response

@then('the response status code should be 200')
def check_status():
    assert shared["response"].status_code == 200

@then('the response should contain a token')
def check_token():
    assert "token" in shared["response"].json()
