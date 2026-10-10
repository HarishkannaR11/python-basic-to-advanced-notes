import pytest

from control_flow_ex import collatz_steps, fizzbuzz, grade, is_prime, sum_of_multiples


def test_fizzbuzz():
    assert fizzbuzz(15) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
        "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz",
    ]
    assert fizzbuzz(0) == []


def test_sum_of_multiples():
    assert sum_of_multiples(10) == 23
    assert sum_of_multiples(1000) == 233168


@pytest.mark.parametrize("n, expected", [(0, False), (1, False), (2, True), (9, False), (97, True)])
def test_is_prime(n, expected):
    assert is_prime(n) is expected


def test_collatz_steps():
    assert collatz_steps(1) == 0
    assert collatz_steps(6) == 8
    assert collatz_steps(27) == 111


@pytest.mark.parametrize(
    "score, expected",
    [(100, "A"), (90, "A"), (89, "B"), (75, "C"), (60, "D"), (59, "F"), (0, "F")],
)
def test_grade(score, expected):
    assert grade(score) == expected
