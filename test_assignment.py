import pytest
import inspect
from assignment import extract_emails, mask_credit_card_numbers, find_duplicate_characters

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

@pytest.mark.parametrize("input, expected", [
    ("Contact us at support@example.com or admin@example.org", ["support@example.com", "admin@example.org"]),
    ("No emails here!", []),
    ("My email is staff@example.com", ["staff@example.com"]),
    ("Reach out: john.doe@mail.com and jane_doe123@workplace.org", ["john.doe@mail.com", "jane_doe123@workplace.org"]),
    ("", [])
])
def test1(input, expected):
    assert extract_emails(input) == expected
    assert check_contains_loop(extract_emails)

@pytest.mark.parametrize("input, expected", [
    ("My credit card is 1234567812345678", "****-****-****-5678"),
    ("No card here.", ""),
    ("My card number is 9988776612347869", "****-****-****-7869"),
    ("", "")
])
def test2(input, expected):
    assert mask_credit_card_numbers(input) == expected
    assert check_contains_loop(mask_credit_card_numbers)

@pytest.mark.parametrize("input, expected", [
    ("programming", ['r', 'g', 'm']),
    ("hello", ['l']),
    ("abcdef", []),
    ("aabbcc", ['a', 'b', 'c']),
    ("", [])
])
def test3(input, expected):
    assert find_duplicate_characters(input) == expected
    assert check_contains_loop(find_duplicate_characters)
