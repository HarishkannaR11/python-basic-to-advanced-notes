# Stage 1 mini-projects

Do these after the exercises. Write each as a single script (`python project.py`) and keep it
under about 100 lines. There are no tests: you decide when it works.

## 1. Number guessing game
The computer picks a random number 1 to 100 (`import random`; `random.randint(1, 100)`).
The player guesses; respond "higher" or "lower" and count attempts. Handle non-numeric input
without crashing.
**Practises:** loops, conditions, input, `try / except ValueError`.

## 2. To-do list (in memory)
A menu loop: add task, list tasks, mark done, delete task, quit. Store tasks as a list of dicts
(`{"title": ..., "done": False}`).
**Practises:** lists, dicts, functions, string formatting.
*Stretch:* save to and load from a `tasks.json` file (`import json`).

## 3. Word-frequency analyser
Read a text file, then print the 10 most common words (ignore case and punctuation) in a neat table.
**Practises:** file reading (`with open(...)`), dicts, sorting by value (`sorted(d.items(), key=...)`).

## 4. Simple calculator
Ask for two numbers and an operator (`+ - * /`); print the result; keep going until the user types `q`.
Handle divide by zero politely.
**Practises:** functions, conditions, exceptions.

## 5. Contact book
Store name, phone and email for each contact. Search by partial name, edit, delete.
**Practises:** dicts of dicts, comprehensions, functions.

When you finish stage 1, move to `02_intermediate/`.
