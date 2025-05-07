import pytest

def reverse_and_append(lst, item):
    reversed_list = lst[::-1]
    reversed_list.append(item)
    return reversed_list

def test_reverse_and_append():
    lst = [1, 2, 3]
    item = 4
    result = reverse_and_append(lst, item)
    expected = [3, 2, 1, 4]
    assert result == expected, "The list should be reversed and the item appended"

def test_empty_list():
    lst = []
    item = 5
    result = reverse_and_append(lst, item)
    expected = [5]
    assert result == expected, "Appending to an empty list should return a list with just the item"

def test_list_of_strings():
    lst = ["a", "b", "c"]
    item = "d"
    result = reverse_and_append(lst, item)
    expected = ["c", "b", "a", "d"]
    assert result == expected, "Should reverse the list of strings and append the new string"
