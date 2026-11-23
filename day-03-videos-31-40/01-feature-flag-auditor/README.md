# Feature Flag Rollout Auditor

**Day:** 03 · **Difficulty:** Hard  
**Topics:** Dictionary methods, copying, strings, Boolean operators, comparisons

## Problem Description

You maintain an API configuration. Apply a release update to a separate working configuration, inspect a default, and evaluate a rollout policy. Do not mutate the original top-level dictionary.

## Given

```python
settings = {
    "app_name": "  rAjeAA--API  ",
    "environment": "staging",
    "version": "2.4.1",
    "requests_limit": 2000,
    "requests_used": 1475,
    "features": {"audit_logs": True, "beta_access": False}
}

changes = {"environment": "production", "requests_limit": 3500}

audit = {"status": "pending", "reviewer": "backend", "build": "2026.11"}
```

## Requirements

1. Create a shallow copy of `settings` named `working` so top-level changes do not modify the original.
2. Normalize the app name in `working` to `rajeaa-api` (remove outer spaces, lowercase, replace `--` with `-`).
3. Apply all entries from `changes` to `working` using a Dictionary Method.
4. Add a `region` key with default value `me-central` only if it is absent.
5. Read `timeout_seconds` with fallback `30` **without inserting that key**.
6. Remove the old `version` field from `working` and store the removed value.
7. Remove and capture the most recently inserted pair from the separate `audit` dictionary.
8. Calculate remaining requests (`limit - used`).
9. Calculate `quota_healthy`: used requests are strictly less than the limit.
10. Calculate `beta_rollout_allowed`: production environment **AND** healthy quota **AND** audit logs enabled **AND NOT** beta already enabled.
11. Display original vs working environment, and verify the original still has six top-level keys.

## Expected Output

```text
APP: rajeaa-api
Original Environment: staging
Working Environment: production
Region: me-central
Timeout Fallback: 30
Removed Version: 2.4.1
Last Audit Pair: ('build', '2026.11')
Remaining Requests: 2025
Quota Healthy: True
Beta Rollout Allowed: True
Original Key Count: 6
```

## Constraints

- Do not modify `settings` directly.
- Do not modify the nested `features` dictionary; a shallow copy is sufficient for this task.
- Use `get()`, `setdefault()`, `update()`, `pop()`, and `popitem()` meaningfully.
- No `if`, loops, comprehensions, membership operators, or custom functions.

## My Approach

<!-- Write your reasoning here AFTER attempting the problem. -->

## Solutions

- [Solution 1](solution_1.py) — My first independent implementation.
- Add `[Solution 2](solution_2.py)` if you create a distinct approach.

## What I Learned

<!-- Record mistakes, trade-offs, and lessons here. -->
