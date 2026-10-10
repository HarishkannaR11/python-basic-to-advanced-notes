from datetime import date


def extract_emails(text: str) -> list[str]:
    """Return all email addresses found in `text`, in order of appearance.

    Keep it simple: something like `name@domain.tld` where name and domain
    use letters, digits, dots, underscores, hyphens or plus signs.
    """
    raise NotImplementedError


def parse_date(s: str) -> date:
    """Parse 'YYYY-MM-DD' into a date."""
    raise NotImplementedError


def days_between(a: str, b: str) -> int:
    """Whole days from date string `a` to date string `b` (negative if b < a)."""
    raise NotImplementedError


def is_weekend(s: str) -> bool:
    """True if the 'YYYY-MM-DD' date falls on a Saturday or Sunday."""
    raise NotImplementedError
