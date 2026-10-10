import re
from datetime import date

_EMAIL = re.compile(r"[A-Za-z0-9._+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+")


def extract_emails(text: str) -> list[str]:
    return _EMAIL.findall(text)


def parse_date(s: str) -> date:
    return date.fromisoformat(s)


def days_between(a: str, b: str) -> int:
    return (parse_date(b) - parse_date(a)).days


def is_weekend(s: str) -> bool:
    return parse_date(s).weekday() >= 5
