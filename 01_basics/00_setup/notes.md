# Setup: running Python

## Install
Get Python 3.11 or newer from https://www.python.org/downloads/ and check it:

```bash
python --version        # on some systems: python3 --version
```

## Three ways to run code
1. **Interactive prompt (REPL):** type `python`, then try `2 + 2`. Exit with `exit()`.
   Great for quick experiments.
2. **Script:** save code in `hello.py` and run `python hello.py`.
3. **Editor/IDE:** VS Code with the Python extension, or PyCharm.

## Your first script

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

## Reading errors
Python tells you the file, the line and the kind of error. Read the **last line** of a traceback first:
- `SyntaxError`: you typed something Python can't parse (missing colon, bracket, quote).
- `NameError`: you used a name that doesn't exist (typo, or used before defining).
- `TypeError`: wrong kind of value (e.g. `"5" + 3`).
- `IndentationError`: lines in a block aren't aligned.

## Set up this repo

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Then run a topic's tests, for example: `pytest 01_basics/01_variables_types`.
