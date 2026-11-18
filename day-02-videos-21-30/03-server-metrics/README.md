# Immutable Server Metrics

**Difficulty:** Hard  
**Topics:** Tuples, tuple unpacking, slicing, count, index, arithmetic, strings  
**Status:** Not solved

## Problem

Analyze a fixed server session record, create an extended sequence of readings, and calculate recent average performance.

## Given

```python
session = (
    "SRV-19",
    "  api_gateway  ",
    (120, 135, 135, 140, 135, 125),
    "2026-11-18"
)
```

## Requirements

1. Use tuple unpacking to assign the server ID, service name, readings tuple, and date to separate variables.
2. Normalize the service name as `Api Gateway`.
3. Count occurrences of `135` in the original readings tuple.
4. Find the index of its first appearance.
5. Create a new tuple with a reading `150` appended; do not change the original tuple.
6. Slice out the last three readings from the new tuple.
7. Calculate the mean of those three numbers without loops or `sum()`.
8. Print the mean to exactly two decimal places.

## Expected output

```text
SERVER: SRV-19
SERVICE: Api Gateway
DATE: 2026-11-18

135 Occurrences: 3
First 135 Index: 1

Original: (120, 135, 135, 140, 135, 125)
Updated: (120, 135, 135, 140, 135, 125, 150)

Last 3: (135, 125, 150)
Last 3 Average: 136.67
```

## Constraints

Do not convert the readings tuple into a list and mutate it. No loops, conditions, custom functions, or hardcoded results.

## Extra challenge

Explain why `(150)` is not equivalent to `(150,)` in Python.

## My approach

_To fill in after solving: What approach did I choose, and why?_

## Solutions

| Solution | Technique | Notes |
| --- | --- | --- |
| [Solution 1](solution_1.py) | _To fill in_ | _To fill in_ |

> If you develop a genuinely different approach, create `solution_2.py` and add it to this table.

## What I learned

_To fill in: concepts reinforced, mistakes corrected, edge cases, and improvements._
