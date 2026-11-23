# Predict the Output — Dictionary & Boolean Traps

**Day:** 03 · **Difficulty:** Challenging (Bonus)  
**Topics:** Dictionary mutability, alias versus copy, method return values, numeric conversion, Boolean short-circuiting

## Problem Description

This problem is about **reasoning**. Before running the Python file, write the exact value of every printed line in this README. Explain your reasoning for aliasing, conversion, returns, and Boolean expressions.

## Given

```python
settings = {"attempts": "3", "active": True}
alias = settings
snapshot = settings.copy()

new_region = settings.setdefault("region", "eu")
old_attempts = settings.setdefault("attempts", 99)

settings["attempts"] = int(settings["attempts"])
settings["attempts"] += 2

update_result = settings.update({"enabled": False})
last_pair = settings.popitem()

check = (settings["attempts"] >= 5 and settings["active"]) or (
    not settings.get("enabled", False)
)

print(new_region)
print(old_attempts)
print(snapshot["attempts"])
print(alias["attempts"])
print(update_result)
print(last_pair)
print(check)
print((0 or "ready") and not "")
print(settings.get("missing", "none"))
```

## Requirements

1. Without running the code, predict all **nine** `print()` outputs **in order**.
2. Distinguish `alias = settings` from `snapshot = settings.copy()`.
3. Explain what `setdefault()` returns when the key already exists versus missing.
4. Explain why `update_result` is not a dictionary.
5. Track what `popitem()` removed and how the Boolean expression behaves after removal.
6. Explain the result of `or` / `and` / `not`, including operand-return behavior for `or`.
7. Only after saving predictions to the README: run `solution_1.py` and correct your analysis if needed.

## Expected Output

```text
Not supplied intentionally. Predict the nine output lines yourself before running the file.
```

## Constraints

- No editing the source code until after you have committed predictions.
- Do not consult a completed solution.
- Record explanations, not just raw answers.

## My Approach

<!-- Write your reasoning here AFTER attempting the problem. -->

## Solutions

- [Solution 1](solution_1.py) — My first independent implementation.
- Add `[Solution 2](solution_2.py)` if you create a distinct approach.

## What I Learned

<!-- Record mistakes, trade-offs, and lessons here. -->

## My Predictions (complete before execution)

| Print # | Predicted output | Reasoning |
|---|---|---|
| 1 | _Fill in_ | _Explain_ |
| 2 | _Fill in_ | _Explain_ |
| 3 | _Fill in_ | _Explain_ |
| 4 | _Fill in_ | _Explain_ |
| 5 | _Fill in_ | _Explain_ |
| 6 | _Fill in_ | _Explain_ |
| 7 | _Fill in_ | _Explain_ |
| 8 | _Fill in_ | _Explain_ |
| 9 | _Fill in_ | _Explain_ |
