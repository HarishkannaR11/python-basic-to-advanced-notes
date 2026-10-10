# Python: from intermediate to advanced

A hands-on learning path that starts at the fundamentals and ends at advanced Python
(decorators, generators, asyncio, packaging). Every topic has short **notes**, a set of
**exercise stubs** to implement, and **pytest tests** that tell you when you got it right. Reference solutions live in
`solutions/`, so try first and peek only when stuck.

## How to use this repo

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

pytest 01_basics/01_variables_types    # run one topic
pytest                           # run everything
```

1. Read the topic's `notes.md`.
2. Open the exercise file (e.g. `oop.py`) and replace each `raise NotImplementedError` with your code.
3. Run that topic's tests until they pass.
4. Compare with `solutions/<same_file_name>.py`, then note anything you'd do differently.

Tests fail at first on purpose: that is your to-do list.

## Roadmap

### Stage 1: Basics (`01_basics/`)
- [ ] 00 Setup: running Python and reading errors (notes)
- [ ] 01 Variables, types, operators (`variables_ex.py`)
- [ ] 02 Strings (`strings_ex.py`)
- [ ] 03 Control flow (`control_flow_ex.py`)
- [ ] 04 Lists, tuples, dicts, sets (`collections_ex.py`)
- [ ] 05 Functions (`functions_ex.py`)
- [ ] 06 Comprehensions (`comprehensions_ex.py`)
- [ ] 07 Mini-projects (guessing game, to-do list, word counter, ...)

### Stage 2: Intermediate (`02_intermediate/`)
- [ ] 01 Files, JSON, CSV (`files_json.py`)
- [ ] 02 Exceptions (`exceptions_ex.py`)
- [ ] 03 Object-oriented programming (`oop.py`)
- [ ] 04 Regex and dates (`regex_dates.py`)
- [ ] 05 Modules, virtual environments, tooling (notes and practice)

### Stage 3: Advanced (`03_advanced/`)
- [ ] 01 Decorators (`decorators_ex.py`)
- [ ] 02 Iterators and generators (`generators_ex.py`)
- [ ] 03 Context managers (`context_managers_ex.py`)
- [ ] 04 Type hints and dataclasses (`models.py`)
- [ ] 05 asyncio (`async_ex.py`)
- [ ] 06 Threads, processes and the GIL (notes and practice)

### Stage 4: Professional practice (`04_professional_practice/`)
- [ ] Testing, logging, debugging, linting, git workflow, packaging, profiling

### Stage 5: Projects (`05_projects/`)
- [ ] Expense CLI
- [ ] Concurrent web scraper
- [ ] REST API with FastAPI
- [ ] Market regime toolkit (capstone)

## Suggested pace
About 2 to 3 topics per week. Spend as much time on the projects as on the exercises, because
projects are where the concepts stick.

## Layout

```
01_basics/<topic>/         notes.md, exercise file, test file
02_intermediate/<topic>/   notes.md, exercise file, test file
03_advanced/<topic>/       notes.md, exercise file, test file
04_professional_practice/  README.md
05_projects/               README.md (project briefs)
solutions/                 reference solutions, one file per exercise
```

Exercise file names are unique across the repo so pytest can run everything in one go.
