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
