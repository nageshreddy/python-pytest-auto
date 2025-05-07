import pytest
from app import db_handler

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
