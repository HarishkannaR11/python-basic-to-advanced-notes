# Control flow

## Conditions
```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```
Indentation (4 spaces) defines the block. "Falsy" values: `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`, `False`.
Everything else is truthy.

## Loops
```python
for i in range(5):            # 0..4
    print(i)

for index, item in enumerate(["a", "b"], start=1):
    print(index, item)

n = 10
while n > 0:
    n -= 3
```
- `break` leaves the loop; `continue` skips to the next iteration.
- `range(start, stop, step)`: `range(10, 0, -2)` gives 10, 8, 6, 4, 2.
- Loop over things directly (`for x in items`), not over indexes, unless you need the index.

## Ternary expression
`label = "even" if n % 2 == 0 else "odd"`

## Exercises
Implement `control_flow_ex.py`, then `pytest 01_basics/03_control_flow`.
