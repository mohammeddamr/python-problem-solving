# API Deployment Readiness Report

**Difficulty:** Challenging  
**Topics:** Nested dictionaries, tuples, lists, sets, strings, modulo, floor division  
**Status:** Not solved

## Problem

Analyze a backend service configuration, repair its set of API routes, and format deployment health data.

## Given

```python
config = {
    "service": {
        "name": "  PAYMENTS--API  ",
        "version": (2, 5, 0)
    },
    "routes": [
        "/pay",
        "/refund",
        "/pay",
        "/status",
        "/legacy"
    ],
    "required": {
        "/pay", "/refund", "/status", "/health"
    },
    "deprecated": {"/legacy"},
    "uptime_seconds": 92865
}
```

## Requirements

1. Normalize the service name to `payments-api`.
2. Format the version tuple as `2.5.0`.
3. Count original routes and occurrences of `/pay`.
4. Determine how many unique routes exist.
5. Find required routes missing from the current routes.
6. Find deprecated routes that are currently present.
7. Build a corrected route set by removing deprecated routes and adding missing required routes.
8. Verify the corrected routes include everything required and nothing deprecated.
9. Display the final routes sorted alphabetically in a list.
10. Convert uptime seconds to days, hours, minutes and seconds; print clock values using two-digit formatting.

## Expected output

```text
======= DEPLOYMENT REPORT =======
Service: payments-api
Version: 2.5.0

Original Route Count: 5
Unique Route Count: 4
/pay Occurrences: 2

Missing: {'/health'}
Deprecated: {'/legacy'}

Final Routes:
['/health', '/pay', '/refund', '/status']

All Required Present: True
No Deprecated Routes: True

Server Uptime: 1 days, 01:47:45
=================================
```

## Constraints

No loops, conditions, user-defined functions, or video 31+ concepts. Preserve the original `config["routes"]` list. Set output order is not guaranteed, so sort the final display list.

## Extra challenge

Compare an approach based on set subtraction with another based on set `difference_update()` / `update()`.

## My approach

_To fill in after solving: What approach did I choose, and why?_

## Solutions

| Solution | Technique | Notes |
| --- | --- | --- |
| [Solution 1](solution_1.py) | _To fill in_ | _To fill in_ |

> If you develop a genuinely different approach, create `solution_2.py` and add it to this table.

## What I learned

_To fill in: concepts reinforced, mistakes corrected, edge cases, and improvements._
