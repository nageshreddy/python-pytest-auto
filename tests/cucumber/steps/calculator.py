
import pytest

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def get_result(self):
        return self.result

@pytest.fixture
def calculator():
    return Calculator()
