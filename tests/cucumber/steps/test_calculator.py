from pytest_bdd import given, when, then, scenarios, parsers

scenarios('../features/calculator.feature')


@given(parsers.parse('I have entered {number:d} into the calculator'))
def enter_number(calculator, number):
    if not hasattr(calculator, 'inputs'):
        calculator.inputs = []
    calculator.inputs.append(number)


@when('I press add')
def press_add(calculator):
    calculator.add(*calculator.inputs)


@then(parsers.parse('the result should be {expected:d} on the screen'))
def check_result(calculator, expected):
    assert calculator.get_result() == expected
