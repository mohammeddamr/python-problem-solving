# Predict the Output — Mutability Trap

**Difficulty:** Challenging · Bonus  
**Topics:** Lists, copying, in-place methods, tuples, sets, dictionaries, indexing  
**Status:** Not solved

## Problem

Trace in-place mutations and returned values without running the code first.

## Given

```python
a = [3, 1, 3, 2]
b = a.copy()

removed = a.remove(3)

a.sort()
b.reverse()

pair = ("api",) * 2 + ("db",)

permissions = {"read", "write"}
returned = permissions.update({"deploy"})

data = {
    "level": 1,
    "level": 2,
    "scores": b
}

print(a)
print(b)
print(removed)
print(pair.count("api"))
print(pair[-1])
print(returned)
print(permissions.issuperset({"read", "deploy"}))
print(data["level"], data["scores"][0])
```

## Requirements

1. Before running the file, predict the output of **all eight** `print()` statements.
2. Write the predicted output and your explanation in this README.
3. Explain why editing `a` does not edit `b`.
4. Explain the values returned by `remove()` and `update()`.
5. Explain the resulting tuple expression stored in `pair`.
6. Explain what happens when the same dictionary key is specified twice.
7. Run `solution_1.py` to check your predictions, then write a short reflection.

## Expected output

```text
Predict all eight printed lines before executing `solution_1.py`.
Do not replace the prediction with the actual output until you have compared them.
```

## Constraints

This is a prediction task. Do not run the code or use the Python interpreter until after your prediction has been recorded.

## Extra challenge

Give an example of a method that mutates a list in place and a different operation that creates a new list.

## My predicted output (complete before running)

```text
# Replace with your own predictions
```

## Why I predict this

_Explain the eight print outputs step-by-step before executing the file._

## Solutions

| Solution | Technique | Notes |
| --- | --- | --- |
| [Solution 1](solution_1.py) | _To fill in_ | _To fill in_ |

> If you develop a genuinely different approach, create `solution_2.py` and add it to this table.

## What I learned

_To fill in: concepts reinforced, mistakes corrected, edge cases, and improvements._
