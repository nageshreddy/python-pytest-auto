

def test_playground():
    assert True
    # This is a placeholder test function for the playground.
    # You can add your test cases here to experiment with pytest.
    # For example:
    assert 1 + 1 == 2
    # assert "hello".upper() == "HELLO"
    # You can also use fixtures, parametrize, and other pytest features.
def test_list_example():
    my_list = [1, 2, 3]
    assert len(my_list) == 3
    assert my_list[0] == 1
    assert my_list[-1] == 3

def test_dict_example():
    my_dict = {"a": 1, "b": 2}
    assert my_dict["a"] == 1
    assert "b" in my_dict
    assert len(my_dict) == 2
def test_set_example():
    my_set = {1, 2, 3}
    assert len(my_set) == 3
    assert 1 in my_set
    assert 4 not in my_set

def test_tuple_example():
    my_tuple = (1, 2, 3)
    assert len(my_tuple) == 3
    assert my_tuple[0] == 1
    assert my_tuple[-1] == 3

def test_iterate_list():
    my_list = [1, 2, 3]
    for i, value in enumerate(my_list):
        print(f"Index: {i}, Value: {value}")
        assert value == my_list[i]

def test_int_string_conversion():
    my_int = 42
    my_str = str(my_int)
    assert my_str == "42"
    assert isinstance(my_str, str)

def test_string_int_conversion():
    my_str = "42"
    my_int = int(my_str)
    assert my_int == 42
    assert isinstance(my_int, int)

def test_list_comprehension():
    my_list = [x * 2 for x in range(5)]
    assert my_list == [0, 2, 4, 6, 8]

def test_dict_comprehension():
    my_dict = {x: x * 2 for x in range(5)}
    assert my_dict == {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

def test_set_comprehension():
    my_set = {x * 2 for x in range(5)}
    assert my_set == {0, 2, 4, 6, 8}

def test_tuple_examples():
    my_tuple = (1, 2, 3)
    assert len(my_tuple) == 3
    assert my_tuple[0] == 1
    assert my_tuple[-1] == 3

def test_third_highest():
    my_list = [1, 3, 41, 35, 47, 12, 45, 17, 19, 67, 58, 98, 100, 88, 93, 94, 95, 96]
    sorted_list = sorted(my_list, reverse=True)
    third_highest = sorted_list[2]
    print(third_highest)

def test_third_highest_loop():
    my_list = [1, 3, 41, 35, 47, 12, 45, 17, 19, 67, 58, 98, 100, 88, 93, 94, 95, 96, 97]

    first = second = third = float('-inf')

    for num in my_list:
        if num > first:
            third = second
            second = first
            first = num
        elif first > num > second:
            third = second
            second = num
        elif second > num > third:
            third = num

    print(third)
