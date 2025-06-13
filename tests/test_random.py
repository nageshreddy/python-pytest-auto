def test_find_highest_number():
    from random import randint

    def find_highest_number(numbers):
        return max(numbers)

    # Generate a list of random numbers
    random_numbers = [randint(1, 100) for _ in range(10)]

    # Find the highest number using the function
    highest_number = find_highest_number(random_numbers)

    # Assert that the highest number is indeed the maximum in the list
    assert highest_number == max(random_numbers)

