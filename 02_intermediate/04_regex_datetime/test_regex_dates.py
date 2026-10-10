from datetime import date

from regex_dates import days_between, extract_emails, is_weekend, parse_date


def test_extract_emails():
    text = "Contact ada@lovelace.org or bob.smith+news@mail-co.com; not this@ one."
    assert extract_emails(text) == ["ada@lovelace.org", "bob.smith+news@mail-co.com"]


def test_extract_emails_none():
    assert extract_emails("nothing here") == []


def test_parse_date():
    assert parse_date("2020-03-23") == date(2020, 3, 23)


def test_days_between():
    assert days_between("2020-02-20", "2020-03-23") == 32
    assert days_between("2020-03-23", "2020-02-20") == -32


def test_is_weekend():
    assert is_weekend("2020-03-21") is True   # Saturday
    assert is_weekend("2020-03-22") is True   # Sunday
    assert is_weekend("2020-03-23") is False  # Monday
