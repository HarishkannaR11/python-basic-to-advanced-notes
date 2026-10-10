# Strings

Strings are immutable sequences of characters.

```python
s = "Hello, World"
s[0]        # 'H'
s[-1]       # 'd'
s[0:5]      # 'Hello'   (slice: start inclusive, stop exclusive)
s[::-1]     # 'dlroW ,olleH'   (reverse)
len(s)      # 12
```

## Useful methods
`.lower()` `.upper()` `.title()` `.strip()` `.split()` `" ".join(list)` `.replace(a, b)`
`.startswith()` `.endswith()` `.find()` `.count()` `.isdigit()` `.isalpha()` `.isalnum()`

## f-strings
```python
name, score = "Ada", 93.456
f"{name} scored {score:.1f}"     # 'Ada scored 93.5'
f"{1234567:,}"                   # '1,234,567'
f"{name!r}"                      # "'Ada'"
```

## Remember
- Methods return a **new** string; they never change the original.
- `"-" * 20` repeats a string; `"a" in "banana"` tests for a substring.
- Escape sequences: `\n` newline, `\t` tab. Raw strings: `r"C:\path"`.

## Exercises
Implement `strings_ex.py`, then `pytest 01_basics/02_strings`.
