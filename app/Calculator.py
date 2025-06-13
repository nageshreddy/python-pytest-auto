# app/calculator.py.py

class Calculator:
    def __init__(self):
        self.result = 0

    def enter_number(self, number):
        if not hasattr(self, 'numbers'):
            self.numbers = []
        self.numbers.append(number)

    def add(self):
        self.result = sum(self.numbers)

    def get_result(self):
        return self.result
