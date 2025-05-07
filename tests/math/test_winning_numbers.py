import random
import pytest

def buy_ticket():
    return sorted(random.sample(range(1, 50), 6))

def draw_winning_numbers():
    return sorted(random.sample(range(1, 50), 6))

def check_ticket(ticket, winning_numbers):
    return len(set(ticket) & set(winning_numbers))

def test_buy_ticket_length_and_range():
    ticket = buy_ticket()
    assert len(ticket) == 6
    assert all(1 <= num <= 49 for num in ticket)
    assert len(set(ticket)) == 6  # Ensure no duplicates

def test_draw_winning_numbers_length_and_range():
    winning_numbers = draw_winning_numbers()
    assert len(winning_numbers) == 6
    assert all(1 <= num <= 49 for num in winning_numbers)
    assert len(set(winning_numbers)) == 6

def test_check_ticket_matching_count():
    ticket = [1, 2, 3, 4, 5, 6]
    winning_numbers = [4, 5, 6, 7, 8, 9]
    matches = check_ticket(ticket, winning_numbers)
    assert matches == 3  # 4, 5, 6 are common

@pytest.mark.parametrize(
    "ticket, winning_numbers, expected_matches",
    [
        ([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], 0),
        ([10, 20, 30, 40, 50, 49], [10, 20, 30, 40, 50, 49], 6),
        ([1, 2, 3, 4, 5, 6], [6, 7, 8, 9, 10, 11], 1),
    ]
)
def test_check_ticket_parametrized(ticket, winning_numbers, expected_matches):
    assert check_ticket(ticket, winning_numbers) == expected_matches
