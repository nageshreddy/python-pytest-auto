import psycopg2
import pytest
import psycopg2
from faker import Faker
# Database connection config
DB_CONFIG = {
    'dbname': 'mydb',         # Your DB name
    'user': 'postgres',          # Your username
    'password': 'ayrareddy', # Your password
    'host': 'localhost',
    'port': '5432'
}

# Pytest fixture to connect to the database
@pytest.fixture(scope="module")
def db_conn():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    yield cur, conn
    cur.close()
    conn.close()

def test_create_table(db_conn):
    cur, conn = db_conn
    cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(100),
        age INTEGER,
        department VARCHAR(50),
        salary NUMERIC(10, 2),
        city VARCHAR(100),
        country VARCHAR(100)
    )
    """)
    conn.commit()
    # Check if table exists
    cur.execute("""
    SELECT EXISTS (
        SELECT FROM information_schema.tables 
        WHERE table_name = 'employees'
    )
    """)
    exists = cur.fetchone()[0]
    assert exists is True

def test_insert_1000_employees(db_conn):
    cur, conn = db_conn
    fake = Faker()
    for _ in range(1000):
        full_name = fake.name()
        age = fake.random_int(min=20, max=65)
        department = fake.random_element(elements=('HR', 'Engineering', 'Sales', 'Marketing', 'Finance', 'Support'))
        salary = round(fake.random_number(digits=5), 2)
        city = fake.city()
        country = fake.country()

        cur.execute("""
        INSERT INTO employees (full_name, age, department, salary, city, country)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (full_name, age, department, salary, city, country))

    conn.commit()

    # Verify 1000 rows were inserted (you might want to clean before the test!)
    cur.execute("SELECT COUNT(*) FROM employees")
    count = cur.fetchone()[0]
    assert count >= 1000  # If table was empty before, it will be exactly 1000
