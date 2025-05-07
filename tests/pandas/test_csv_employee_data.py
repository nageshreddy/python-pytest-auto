import pandas as pd
from faker import Faker
import pytest
import os

class EmployeeDataHandler:
    def __init__(self, filename='employees.csv'):
        self.filename = filename
        self.fake = Faker()

    def generate_and_save_csv(self, record_count=500):
        employees = []

        for _ in range(record_count):
            full_name = self.fake.name()
            age = self.fake.random_int(min=20, max=65)
            department = self.fake.random_element(elements=('HR', 'Engineering', 'Sales', 'Marketing', 'Finance', 'Support'))
            salary = round(self.fake.random_int(min=30000, max=120000), 2)
            city = self.fake.city()
            country = self.fake.country()

            employees.append({
                "Full Name": full_name,
                "Age": age,
                "Department": department,
                "Salary": salary,
                "City": city,
                "Country": country
            })

        df = pd.DataFrame(employees)
        df.to_csv(self.filename, index=False)
        return df

    def read_csv(self):
        df = pd.read_csv(self.filename)
        return df


# 🔍 Pytest tests
@pytest.fixture(scope="module")
def data_handler():
    handler = EmployeeDataHandler('/Users/nageshmallareddypro/PycharmProjects/pytest-auto-main/tests/pandas/employees.csv')
    yield handler
    # Clean up the CSV file after tests
    if os.path.exists(handler.filename):
        os.remove(handler.filename)


def test_generate_csv(data_handler):
    df = data_handler.generate_and_save_csv(500)
    assert len(df) == 500
    assert set(df.columns) == {"Full Name", "Age", "Department", "Salary", "City", "Country"}


def test_read_csv(data_handler):
    df = data_handler.read_csv()
    assert not df.empty
    assert len(df) == 500
    assert 'Full Name' in df.columns
    assert 'Salary' in df.columns
