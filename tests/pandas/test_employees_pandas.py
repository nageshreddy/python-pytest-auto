import pytest
import pandas as pd
import psycopg2

DB_CONFIG = {
    'dbname': 'mydb',  # Your DB name
    'user': 'postgres',  # Your username
    'password': 'ayrareddy',  # Your password
    'host': 'localhost',
    'port': '5432'
}

@pytest.fixture(scope="module")
def db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    yield conn
    conn.close()


def test_employees_table_exists_and_has_data(db_connection):
    df = pd.read_sql("SELECT * FROM employees", db_connection)

    #  Check if the table has at least 1 row
    assert len(df) > 0, "Employees table is empty"

    # Check if expected columns exist
    expected_columns = {
        'id', 'full_name', 'age', 'department', 'salary', 'city', 'country'
    }
    assert expected_columns.issubset(df.columns), f"Missing columns: {expected_columns - set(df.columns)}"


def test_employees_data_types(db_connection):
    df = pd.read_sql("SELECT * FROM employees", db_connection)

    # Check types (using pandas dtypes)
    assert df['full_name'].dtype == object
    assert df['age'].dtype in ['int64', 'float64']  # Could be float if NULLs
    assert df['salary'].dtype in ['float64', 'object']  # Postgres NUMERIC may come as object
    assert df['department'].dtype == object
    assert df['city'].dtype == object
    assert df['country'].dtype == object


def test_age_range(db_connection):
    df = pd.read_sql("SELECT * FROM employees", db_connection)

    # Check all ages are between 20 and 65
    invalid_ages = df[~df['age'].between(20, 65)]
    assert invalid_ages.empty, f"Found employees with invalid ages: {invalid_ages[['id', 'age']]}"


def test_salary_positive(db_connection):
    df = pd.read_sql("SELECT * FROM employees", db_connection)

    # Check all salaries are > 0
    invalid_salaries = df[df['salary'] <= 0]
    assert invalid_salaries.empty, f"Found employees with invalid salaries: {invalid_salaries[['id', 'salary']]}"


def test_department_values(db_connection):
    df = pd.read_sql("SELECT * FROM employees", db_connection)

    # Check department values are within expected set
    expected_departments = {'HR', 'Engineering', 'Sales', 'Marketing', 'Finance', 'Support'}
    invalid_departments = df[~df['department'].isin(expected_departments)]
    assert invalid_departments.empty, f"Found employees with invalid departments: {invalid_departments[['id', 'department']]}"


def test_unique_ids(db_connection):
    df = pd.read_sql("SELECT * FROM employees", db_connection)

    # Check all IDs are unique
    duplicate_ids = df[df.duplicated(['id'], keep=False)]
    assert duplicate_ids.empty, f"Found duplicate IDs: {duplicate_ids[['id']]}"


def test_city_country_not_null(db_connection):
    df = pd.read_sql("SELECT * FROM employees", db_connection)

    # Check city and country are not NULL
    null_city = df[df['city'].isnull()]
    null_country = df[df['country'].isnull()]

    assert null_city.empty, f"Found employees with NULL city: {null_city[['id', 'city']]}"
    assert null_country.empty, f"Found employees with NULL country: {null_country[['id', 'country']]}"




def test_department_count(db_connection):
    df = pd.read_sql("SELECT department, COUNT(*) as count FROM employees GROUP BY department", db_connection)

    # Check each department has at least 1 employee
    assert all(df['count'] > 0), "Some departments have no employees"


def test_employee_age_distribution(db_connection):
    df = pd.read_sql("SELECT age FROM employees", db_connection)

    # Check age distribution is reasonable (e.g., no ages below 20 or above 65)
    assert df['age'].min() >= 20, "Found employees with age below 20"
    assert df['age'].max() <= 65, "Found employees with age above 65"


def test_employee_city_distribution(db_connection):
    df = pd.read_sql("SELECT city FROM employees", db_connection)

    # Check city distribution is reasonable (e.g., no empty cities)
    assert df['city'].notnull().all(), "Found employees with NULL city"
    assert df['city'].nunique() > 1, "Not enough unique cities"
    assert df['city'].str.len().max() <= 100, "City names are too long"



def test_employee_country_distribution(db_connection):
    df = pd.read_sql("SELECT country FROM employees", db_connection)

    # Check country distribution is reasonable (e.g., no empty countries)
    assert df['country'].notnull().all(), "Found employees with NULL country"
    assert df['country'].nunique() > 1, "Not enough unique countries"
    assert df['country'].str.len().max() <= 100, "Country names are too long"


def test_employee_salary_distribution(db_connection):
    df = pd.read_sql("SELECT salary FROM employees", db_connection)
    # Check salary distribution is reasonable (e.g., no negative salaries)
    assert (df['salary'] >= 0).all(), "Found employees with negative salaries"
    assert df['salary'].nunique() > 1, "Not enough unique salaries"
    assert df['salary'].max() <= 200000, "Salaries are too high"
    assert df['salary'].min() >= 166.00, "Salaries are too low"

def test_employee_department_distribution(db_connection):
    df = pd.read_sql("SELECT department FROM employees", db_connection)
    # Check department distribution is reasonable (e.g., no empty departments)
    assert df['department'].notnull().all(), "Found employees with NULL department"
    assert df['department'].nunique() > 1, "Not enough unique departments"
    assert df['department'].str.len().max() <= 50, "Department names are too long"
