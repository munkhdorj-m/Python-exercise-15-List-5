import pytest
import inspect
from assignment import sum_of_digits, largest_negative_and_smallest_positive, odd_first_last_digits

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

@pytest.mark.parametrize("numbers, expected", [
    ([12, 23], 8),
    ([12, 23, 43], 15),
    ([113, 234], 14),
    ([1002, 2005], 10)
])
def test1(numbers, expected):
    assert sum_of_digits(numbers) == expected
    assert check_contains_loop(sum_of_digits)

@pytest.mark.parametrize("numbers, expected", [
    ([-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18], [-6, 2]),
    ([-1, -2, -3, -4], [-1, 0]),
    ([1, 2, 3, 4], [0, 1]),
    ([], [0, 0]),
    ([-10, -9, -8, 0, 15, 25], [-8, 15])
])
def test2(numbers, expected):
    assert largest_negative_and_smallest_positive(numbers) == expected
    assert check_contains_loop(largest_negative_and_smallest_positive)

@pytest.mark.parametrize("numbers, expected", [
    ([1, 3, 79, 10, 4, 1, 39, 62], [79, 39]),
    ([11, 31, 77, 93, 48, 1, 57], [11, 31, 77, 93, 57]),
    ([13, 22, 15, 42, 55], [13, 15, 55]),
    ([20, 40, 60, 80], []),
    ([19, 33, 1001, 55, 121], [19, 33, 1001, 55, 121])
])
def test3(numbers, expected):
    assert odd_first_last_digits(numbers) == expected
    assert check_contains_loop(odd_first_last_digits)
