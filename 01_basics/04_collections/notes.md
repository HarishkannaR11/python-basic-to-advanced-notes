# Lists, tuples, dicts and sets

| Type | Literal | Ordered | Mutable | Duplicates | Use it for |
|---|---|---|---|---|---|
| list | `[1, 2, 3]` | yes | yes | yes | sequences you modify |
| tuple | `(1, 2)` | yes | no | yes | fixed records, return values |
| dict | `{"a": 1}` | yes (insertion) | yes | unique keys | lookups by key |
| set | `{1, 2, 3}` | no | yes | no | membership, removing duplicates |

## Lists
```python
nums = [5, 2, 9]
nums.append(1); nums.extend([7, 8]); nums.remove(2); nums.pop()
nums[1:3]; nums[::-1]; len(nums); sorted(nums); nums.sort(reverse=True)
```
`sorted()` returns a new list; `.sort()` sorts in place and returns `None`.

## Dicts
```python
d = {"apple": 3}
d["pear"] = 5
d.get("kiwi", 0)                 # 0, no KeyError
for key, value in d.items(): ...
d.setdefault("fig", []).append(1)
```

## Sets
```python
a, b = {1, 2, 3}, {2, 3, 4}
a | b     # union        {1, 2, 3, 4}
a & b     # intersection {2, 3}
a - b     # difference   {1}
```

## Unpacking
`first, *rest = [1, 2, 3]`, `x, y = (10, 20)`

## Exercises
Implement `collections_ex.py`, then `pytest 01_basics/04_collections`.
