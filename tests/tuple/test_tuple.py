import pytest


def add_element_to_tuple(tpl, element):
    return tpl + (element,)


@pytest.mark.parametrize(
    "tpl, element, expected",
    [
        ((1, 2, 3), 4, (1, 2, 3, 4)),
        ((), 10, (10,)),
        (("x", "y"), "z", ("x", "y", "z")),
    ]
)
def test_add_element_to_tuple(tpl, element, expected):
    result = add_element_to_tuple(tpl, element)
    print(result)
    assert result == expected

def test_add_element_to_tuple_empty():
    result = add_element_to_tuple((), 5)
    assert result == (5,)

def test_add_element_to_tuple_single_element():
    result = add_element_to_tuple((42,), 100)
    assert result == (42, 100)