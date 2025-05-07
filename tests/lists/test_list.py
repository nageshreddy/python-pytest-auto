import pytest


def reverse_and_append(lst, item):
    reversed_list = lst[::-1]
    reversed_list.append(item)
    return reversed_list


@pytest.mark.parametrize(
    "lst, item, expected",
    [
        ([1, 2, 3], 4, [3, 2, 1, 4]),
        ([], 5, [5]),
        (["x", "y"], "z", ["y", "x", "z"]),
    ]
)
def test_reverse_and_append(lst, item, expected):
    result = reverse_and_append(lst, item)
    assert result == expected


def test_list_length():
    lst = [1, 2, 3]
    assert len(lst) == 3, "The list should contain 3 elements"


def test_list_content():
    lst = [1, 2, 3]
    assert lst == [1, 2, 3], "The list should contain the elements 1, 2, and 3"


def test_list_type():
    lst = [1, 2, 3]
    assert isinstance(lst, list), "The variable should be of type list"


def test_list_append():
    lst = [1, 2]
    lst.append(3)
    assert lst == [1, 2, 3], "The list should contain the elements 1, 2, and 3 after appending"


def test_list_pop():
    lst = [1, 2, 3]
    popped_element = lst.pop()
    assert popped_element == 3, "The popped element should be 3"
    assert lst == [1, 2], "The list should contain the elements 1 and 2 after popping"


def test_list_insert():
    lst = [1, 3]
    lst.insert(1, 2)
    assert lst == [1, 2, 3], "The list should contain the elements 1, 2, and 3 after inserting"


def test_list_remove():
    lst = [1, 2, 3]
    lst.remove(2)
    assert lst == [1, 3], "The list should contain the elements 1 and 3 after removing 2"

def test_list_clear():
    lst = [1, 2, 3]
    lst.clear()
    assert lst == [], "The list should be empty after clearing"


def test_list_index():
    lst = [1, 2, 3]
    index = lst.index(2)
    assert index == 1, "The index of element 2 should be 1"


def test_list_count():
    lst = [1, 2, 2, 3]
    count = lst.count(2)
    assert count == 2, "The count of element 2 should be 2"


def test_list_sort():
    lst = [3, 1, 2]
    lst.sort()
    assert lst == [1, 2, 3], "The list should be sorted in ascending order"


def test_list_reverse():
    lst = [1, 2, 3]
    lst.reverse()
    assert lst == [3, 2, 1], "The list should be reversed"


def test_list_copy():
    lst = [1, 2, 3]
    copied_list = lst.copy()
    assert copied_list == [1, 2, 3], "The copied list should be equal to the original list"
    assert copied_list is not lst, "The copied list should not be the same object as the original list"


def test_list_extend():
    lst = [1, 2]
    lst.extend([3, 4])
    assert lst == [1, 2, 3, 4], "The list should contain the elements 1, 2, 3, and 4 after extending"


def test_list_slice():
    lst = [1, 2, 3, 4, 5]
    sliced_list = lst[1:4]
    assert sliced_list == [2, 3, 4], "The sliced list should contain the elements 2, 3, and 4"


def test_list_comprehension():
    lst = [1, 2, 3, 4]
    squared_list = [x ** 2 for x in lst]
    assert squared_list == [1, 4, 9, 16], "The squared list should contain the squares of the original elements"


def test_list_nested():
    lst = [[1, 2], [3, 4]]
    flattened_list = [item for sublist in lst for item in sublist]
    assert flattened_list == [1, 2, 3, 4], "The flattened list should contain all elements from the nested lists"


def test_list_join():
    lst = ["Hello", "World"]
    joined_string = " ".join(lst)
    assert joined_string == "Hello World", "The joined string should be 'Hello World'"


def test_list_find():
    lst = ["apple", "banana", "cherry"]
    index = lst.index("banana")
    assert index == 1, "The index of 'banana' should be 1"
    with pytest.raises(ValueError):
        lst.index("orange")


def test_list_contains():
    lst = [1, 2, 3]
    assert 2 in lst, "The list should contain the element 2"
    assert 4 not in lst, "The list should not contain the element 4"


def test_list_multiply():
    lst = [1, 2]
    multiplied_list = lst * 3
    assert multiplied_list == [1, 2, 1, 2, 1, 2], "The multiplied list should contain the elements repeated 3 times"


def test_list_set_operations():
    lst1 = [1, 2, 3]
    lst2 = [3, 4, 5]

    # Union
    union = list(set(lst1) | set(lst2))
    assert sorted(union) == [1, 2, 3, 4, 5], "The union of the lists should contain all unique elements"

    # Intersection
    intersection = list(set(lst1) & set(lst2))
    assert sorted(intersection) == [3], "The intersection of the lists should contain only the common elements"

    # Difference
    difference = list(set(lst1) - set(lst2))
    assert sorted(difference) == [1, 2], "The difference of the lists should contain elements in lst1 not in lst2"


def test_list_zip():
    lst1 = [1, 2, 3]
    lst2 = ['a', 'b', 'c']
    zipped_list = list(zip(lst1, lst2))
    assert zipped_list == [(1, 'a'), (2, 'b'),
                           (3, 'c')], "The zipped list should contain tuples of corresponding elements"


def test_list_enumerate():
    lst = ['a', 'b', 'c']
    enumerated_list = list(enumerate(lst))
    assert enumerated_list == [(0, 'a'), (1, 'b'),
                               (2, 'c')], "The enumerated list should contain tuples of index and element"


def test_list_find_max():
    lst = [1, 2, 3]
    max_value = max(lst)
    assert max_value == 3, "The maximum value in the list should be 3"


def test_list_find_min():
    lst = [1, 2, 3]
    min_value = min(lst)
    assert min_value == 1, "The minimum value in the list should be 1"


def test_list_sum():
    lst = [1, 2, 3]
    total = sum(lst)
    assert total == 6, "The sum of the list should be 6"


def test_list_average():
    lst = [1, 2, 3]
    average = sum(lst) / len(lst)
    assert average == 2, "The average of the list should be 2"


def test_list_sort_descending():
    lst = [3, 1, 2]
    lst.sort(reverse=True)
    assert lst == [3, 2, 1], "The list should be sorted in descending order"


def test_list_sort_custom():
    lst = ["apple", "banana", "cherry"]
    lst.sort(key=len)
    assert lst == ["apple", "banana", "cherry"], "The list should be sorted by string length"

def test_list_filter():
    lst = [1, 2, 3, 4, 5]
    filtered_list = list(filter(lambda x: x > 2, lst))
    assert filtered_list == [3, 4, 5], "The filtered list should contain elements greater than 2"