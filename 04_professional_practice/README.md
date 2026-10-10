# Professional practice

Work through these in order; each section is a short reading plus a task you do in your own repo.

## 1. Testing with pytest
- Name tests `test_*.py`; use plain `assert`.
- `@pytest.mark.parametrize` for many inputs, fixtures (`@pytest.fixture`) for setup, `tmp_path` for files.
- `monkeypatch` to replace functions/env vars; `pytest.raises` for errors.
- **Task:** add tests for a function from the COVID market project; aim for edge cases (empty data, NaNs).

## 2. Logging instead of print
```python
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger(__name__)
log.info("loaded %d rows", len(df))
```
- Levels: DEBUG < INFO < WARNING < ERROR < CRITICAL. Use `log.exception` inside `except` to keep the traceback.

## 3. Debugging
- `breakpoint()` drops into `pdb`: `n` next, `s` step in, `c` continue, `p expr` print, `q` quit.
- Read tracebacks bottom-up. Reproduce with the smallest possible input first.

## 4. Code quality
- `ruff check .` (lint) and `ruff format .` (format) before every commit.
- Type-check with `mypy` or `pyright` once you add type hints.

## 5. Git workflow
- Small commits with meaningful messages; one branch per feature; open a PR even on your own repo.

## 6. Packaging a project
- Use `pyproject.toml`; layout `src/yourpackage/`; install with `pip install -e .`.
- Pin dependencies in `requirements.txt` or use `uv` / `poetry`.
- Read config from environment variables, never hard-code secrets.

## 7. Performance basics
- Measure before optimising: `timeit`, `cProfile`, `snakeviz`.
- Prefer built-ins, comprehensions, sets for membership tests, `collections.deque` for queues, vectorised NumPy/pandas over Python loops.
