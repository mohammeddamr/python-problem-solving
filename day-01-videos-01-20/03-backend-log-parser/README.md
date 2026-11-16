# Backend Log Parser

**Difficulty:** Hard  
**Topics:** find(), Slicing, Strings  
**Status:** Not solved

## Problem

Backend Log Parser: use the provided inputs to compute the requested results. Build the logic rather than typing the expected output directly.

## Given

```python
log = "  [ERROR] :: service=PAYMENTS :: code=503 :: message=GATEWAY_TIMEOUT  "
```

## Requirements

1. Extract the severity, service, code, and message from the log.
2. Locate field boundaries with `find()` and string slicing rather than fixed offsets.
3. Format the message in title case, replacing the underscore with a space.
4. Display the parsed fields.

## Expected output

```text
Severity: ERROR
Service: payments
Code: 503
Message: Gateway Timeout
```

## Constraints

Do not manually type extracted values into the final output.

## My approach

_To fill in after solving: What idea did I use, and why?_

## Solutions

| Solution | Technique | Notes |
| --- | --- | --- |
| [Solution 1](solution_1.py) | _To fill in_ | _To fill in_ |

> If a second approach is genuinely different, create `solution_2.py` and add a row here comparing the approaches.

## What I learned

_To fill in after solving: important methods, mistakes, edge cases, or improvements._
