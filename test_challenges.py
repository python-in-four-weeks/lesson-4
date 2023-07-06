import pytest

from typing import Sequence

import challenges


def test_is_palindrome_with_invalid_palindrome() -> None:
    palindrome_result = challenges.is_palindrome('grammar')
    assert palindrome_result is False, "The text \"grammar\" should not be classified as a palindrome"


def test_is_palindrome_with_valid_palindrome() -> None:
    raise NotImplementedError("A test for a valid palindrome hasn't been written yet")


@pytest.mark.parametrize('text, expected_palindrome_result', [
    ('grammar', False),
    # Your new test case should go here
])
def test_is_palindrome_parametrized(text: str, expected_palindrome_result: bool) -> None:
    palindrome_result = challenges.is_palindrome(text)
    assert palindrome_result == expected_palindrome_result, f"The text \"{text}\" {'should' if expected_palindrome_result else 'should not'} be classified as a palindrome"


@pytest.mark.parametrize('n, expected_total', [
    (0, 0),
    # Your new test case(s) should go here
])
def test_sum_of_numbers_up_to_n(n: int, expected_total: int) -> None:
    total = challenges.sum_of_numbers_up_to_n(n)
    assert total == expected_total, f"The numbers from 0 to {n} should sum to {expected_total}"


@pytest.mark.parametrize('text, should_be_numeric', [
    ('0', True),
    ('123', True),
    ('-123', True),
    ('123.45', True),
    ('-123.45', True),
    ('123..45', False),
    ('123.45.6', False),
    ('hello', False),
])
def test_is_numeric(text: str, should_be_numeric: bool) -> None:
    raise NotImplementedError("Tests for is_numeric haven't been written yet")


@pytest.mark.parametrize('numbers, should_be_sorted', [
    # Your test cases should go here
])
def test_is_sorted(numbers: Sequence[int], should_be_sorted: bool) -> None:
    raise NotImplementedError("Tests for is_sorted haven't been written yet")


@pytest.mark.parametrize('password_attempt, should_be_successful', [
    # Your test cases should go here
])
def test_login(password_attempt: str, should_be_successful: bool) -> None:
    raise NotImplementedError("Tests for login haven't been written yet")


@pytest.mark.parametrize('wants_to_visit_moon, can_afford_to_visit_moon, should_visit_moon', [
    # Your test cases should go here
])
def test_should_visit_moon(wants_to_visit_moon: str, can_afford_to_visit_moon: str, should_visit_moon: str) -> None:
    raise NotImplementedError("Tests for should_visit_moon haven't been written yet")
