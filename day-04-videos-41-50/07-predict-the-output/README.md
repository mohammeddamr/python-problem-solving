# Predict the Output — While, Aliases & Conditions

**Day:** 04 · **Difficulty:** Challenging — Bonus  
**Topics:** while...else, if/elif, membership, mutation, shallow copy, ternary, Boolean operands

## Problem Description

Don't run this program until you've predicted all nine print calls. Trace the loop by hand: the copy shares a nested list but not subsequent top-level boolean reassignment. Note the difference between a string contained as a full list element and a substring of an element.

## Given

```python
state = {"routes": ["/pay", "/status"], "enabled": True}
shadow = state.copy()
alias = state

requests = ["/pay", "/legacy", "/pay", "/status"]
index = 0
allowed_count = 0

while index < len(requests):
    route = requests[index]

    if route in shadow["routes"] and alias["enabled"]:
        allowed_count += 1
    elif route == "/legacy":
        shadow["routes"].append("/legacy")

    index += 1
else:
    print("FINISHED", index)

print(allowed_count)
print(state["routes"])
print(shadow["routes"] is state["routes"])

alias["enabled"] = False
print(shadow["enabled"])
print(state["enabled"])
print("legacy" in shadow["routes"])
print("ready" if allowed_count >= 3 else "blocked")
print((0 or "online") and not 0)
```

## Requirements

1. Write the exact value printed by **all nine** `print()` calls in the table below **before** running this file.
2. Show a short step-by-step trace of each iteration of the `while` loop.
3. Explain why the `while`'s `else` block executes (or doesn't).
4. Explain the relationship between `state`, `shadow`, and `alias` before and after mutations.
5. Explain the membership result, the ternary result, and the final `and/or` expression.
6. Run the starter file only after saving your predictions; record discrepancies in your README.

## Expected Output

Do **not** look up or copy the expected output. Your task is to predict it.

| Print # | My Prediction | Why? |
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

## Constraints

- Predict first; don't modify the given program before making predictions.
- No `for`, custom functions, or tools for tracing. You can draw a table on paper.
- This bonus intentionally contains no reference answers.

## My Approach

<!-- Explain your approach in your own words AFTER attempting the problem. -->

## Solutions

- [Solution 1](solution_1.py) — My independent attempt.
- Add `[Solution 2](solution_2.py)` if you find a genuinely different approach.

## What I Learned

<!-- Record mistakes, edge cases, and improvements after solving. -->
