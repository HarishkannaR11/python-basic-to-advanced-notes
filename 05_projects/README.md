# Projects

Build these in order. Each one forces you to combine several earlier stages. Put each in its own
folder with its own `README.md`, tests and `requirements.txt`.

## Project 1: Expense CLI (intermediate)
A command-line expense tracker.
- `argparse` subcommands: `add`, `list`, `summary --month 2024-03`.
- Persist to a JSON or CSV file; validate input with custom exceptions.
- Tests for parsing and summary logic.
- **Skills:** files, exceptions, OOP, `datetime`, `argparse`, pytest.

## Project 2: Concurrent web scraper (advanced)
Fetch a list of pages concurrently and extract titles/links.
- Use `asyncio` + `httpx`, with a concurrency limit (`asyncio.Semaphore`) and retries (your decorator).
- Respect `robots.txt`, add timeouts, log failures.
- **Skills:** async, decorators, context managers, logging.

## Project 3: REST API with FastAPI (advanced)
A small API (e.g. notes or portfolio) with CRUD endpoints.
- Pydantic models, SQLite via `sqlite3` or SQLAlchemy, automated tests with `TestClient`.
- **Skills:** typing, dataclasses/pydantic, packaging, testing.

## Project 4: Market regime toolkit (capstone)
Refactor your COVID market regime analysis into a reusable package.
- `src/regimes/` with functions for loading prices, computing returns/volatility, and labelling regimes.
- Type hints throughout, unit tests with small fixture data, a CLI entry point, and a README with charts.
- **Skills:** everything.

## Definition of done
Tests pass, `ruff check .` is clean, README explains how to run it, and a fresh clone works after
`pip install -r requirements.txt`.
