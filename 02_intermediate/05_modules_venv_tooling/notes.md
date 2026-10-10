# Modules, packages, virtual environments

## Modules and packages
- Any `.py` file is a module; a folder with an `__init__.py` is a package.
- `from package.module import name`; avoid `from x import *`.
- `if __name__ == "__main__":` runs code only when the file is executed directly.

## Virtual environments
Each project gets its own isolated set of packages:

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip freeze > requirements.txt      # pin exactly what you have installed
deactivate
```

## Tooling worth learning now
- `pip` / `pip install -e .` for editable installs of your own package.
- `ruff check .` and `ruff format .` for linting and formatting.
- `python -m pdb script.py` or `breakpoint()` to debug.

## Practice
1. Create a `.venv` for this repo and install `requirements.txt`.
2. Run `ruff check .` and read what it tells you.
3. Turn one of your exercise solutions into a small package with an `__init__.py` and import it from a second file.
