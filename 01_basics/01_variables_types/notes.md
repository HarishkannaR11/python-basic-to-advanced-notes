# Variables, types and operators

## Variables
A variable is a name pointing at a value. No type declaration needed.

```python
age = 30            # int
price = 19.99       # float
name = "Ada"        # str
active = True       # bool
nothing = None      # the "no value" value
```

Use `snake_case` names. Check a type with `type(x)`.

## Type conversion
`int("42")`, `float("3.5")`, `str(7)`, `bool(0)` (False). Converting bad input raises `ValueError`.

## Operators
| Kind | Operators |
|---|---|
| Arithmetic | `+ - * / // % **` (`/` true division, `//` floor division, `%` remainder, `**` power) |
| Comparison | `== != < <= > >=` |
| Logical | `and or not` |
| Membership | `in`, `not in` |

```python
7 / 2     # 3.5
7 // 2    # 3
7 % 2     # 1
2 ** 10   # 1024
```

## Handy tricks
- Swap without a temp: `a, b = b, a`
- Round: `round(3.14159, 2)` gives `3.14`
- Floats are approximate: `0.1 + 0.2 != 0.3`. Compare with `math.isclose`.

## Exercises
Implement `variables_ex.py`, then `pytest 01_basics/01_variables_types`.
