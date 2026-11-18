# Backend Ticket Queue Manager

**Difficulty:** Hard  
**Topics:** Lists, indexing, list methods, string methods, copying  
**Status:** Not solved

## Problem

Manage a support ticket queue by cleaning, editing, and sorting a list while preserving the original ticket data.

## Given

```python
tickets = [
    "  auth_failed  ",
    "payment_timeout",
    "auth_failed",
    "profile_updated",
    "db_down"
]
```

## Requirements

1. Save an independent copy of the original list as `original_tickets` before making any changes.
2. Remove surrounding whitespace from the first ticket.
3. Count how many times `auth_failed` appears **after cleaning the first ticket**, before removing a duplicate.
4. Remove exactly **one** occurrence of `auth_failed`.
5. Insert `security_alert` immediately **before** `db_down` without hardcoding the numeric index.
6. Remove `profile_updated` using `pop()` and store the removed value as `resolved_ticket`.
7. Sort the remaining tickets alphabetically.
8. Print the final queue and the unchanged original list.

## Expected output

```text
AUTH FAILED COUNT: 2
RESOLVED: profile_updated

FINAL QUEUE:
['auth_failed', 'db_down', 'payment_timeout', 'security_alert']

ORIGINAL QUEUE:
['  auth_failed  ', 'payment_timeout', 'auth_failed', 'profile_updated', 'db_down']
```

## Constraints

Only use concepts through video 30. Do not use loops, conditions, custom functions, or hardcoded final output. Build the final queue by modifying the input list.

## Extra challenge

Explain why `original_tickets = tickets` would not preserve the original list if you then modify `tickets`.

## My approach

_To fill in after solving: What approach did I choose, and why?_

## Solutions

| Solution | Technique | Notes |
| --- | --- | --- |
| [Solution 1](solution_1.py) | _To fill in_ | _To fill in_ |

> If you develop a genuinely different approach, create `solution_2.py` and add it to this table.

## What I learned

_To fill in: concepts reinforced, mistakes corrected, edge cases, and improvements._
