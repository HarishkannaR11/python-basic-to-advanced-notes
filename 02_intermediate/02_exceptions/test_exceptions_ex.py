import pytest

from exceptions_ex import ValidationError, parse_age, retry, safe_divide


def test_safe_divide():
    assert safe_divide(10, 4) == 2.5
    assert safe_divide(1, 0) is None


@pytest.mark.parametrize("value, expected", [("42", 42), (0, 0), ("150", 150)])
def test_parse_age_ok(value, expected):
    assert parse_age(value) == expected


@pytest.mark.parametrize("value", ["abc", None, -1, 151, "12.5"])
def test_parse_age_bad(value):
    with pytest.raises(ValidationError):
        parse_age(value)


def test_parse_age_chains_cause():
    with pytest.raises(ValidationError) as info:
        parse_age("abc")
    assert isinstance(info.value.__cause__, ValueError)


def test_retry_eventually_succeeds():
    calls = []

    def flaky():
        calls.append(1)
        if len(calls) < 3:
            raise RuntimeError("nope")
        return "ok"

    assert retry(flaky, 5) == "ok"
    assert len(calls) == 3


def test_retry_reraises_last():
    def always_fails():
        raise KeyError("boom")

    with pytest.raises(KeyError):
        retry(always_fails, 2)
