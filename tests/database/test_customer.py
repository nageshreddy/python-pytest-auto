import psycopg2
import pytest

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

# Test to create the customer table
def test_create_customer_table(db_conn):
    cur, conn = db_conn
    cur.execute("""
        DROP TABLE IF EXISTS customer;
        CREATE TABLE customer (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            age INT
        );
    """)
    conn.commit()

    # Check if table exists
    cur.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables
            WHERE table_name = 'customer'
        );
    """)
    assert cur.fetchone()[0] is True

# Test to insert dummy data
def test_insert_customer_data(db_conn):
    cur, conn = db_conn
    cur.execute("""
        INSERT INTO customer (name, email, age) VALUES
        ('Alice Smith', 'alice@example.com', 30),
        ('Bob Johnson', 'bob@example.com', 45),
        ('Carol White', 'carol@example.com', 27);
    """)
    conn.commit()

    # Check row count
    cur.execute("SELECT COUNT(*) FROM customer;")
    assert cur.fetchone()[0] == 3

# Test to query inserted data
def test_query_customer_data(db_conn):
    cur, _ = db_conn
    cur.execute("SELECT * FROM customer ORDER BY id;")
    rows = cur.fetchall()

    assert len(rows) == 12
    assert rows[0][1] == 'Alice Smith'
    assert rows[1][2] == 'bob@example.com'
