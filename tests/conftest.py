import pytest
import requests
from app import db_handler
from tests.cucumber.steps.calculator import Calculator


BASE_URL = "https://videogamedb.uk:443"

@pytest.fixture(scope='module')
def db_conn():
    conn = db_handler.get_db_connection()
    cur = conn.cursor()
    yield cur, conn
    cur.close()
    conn.close()

@pytest.fixture
def sample_csv(tmp_path):
    filepath = tmp_path / "sample.csv"
    data = "name,age\nAlice,30\nBob,25"
    filepath.write_text(data)
    return filepath
# tests/conftest.py

@pytest.fixture
def calculator():
    return Calculator()

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def token(base_url):
    response = requests.post(f"{base_url}/api/authenticate", json={"username": "admin", "password": "admin"})
    return response.json()["token"]