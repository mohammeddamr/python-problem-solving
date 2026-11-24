# Production Incident Monitor

**Day:** 04 · **Difficulty:** Challenging — Capstone  
**Topics:** while, conditions, nested dictionaries, sets, tuples, counters, membership

## Problem Description

You're monitoring an API fleet. Process service events in order and raise a single alert per service when accumulated failures reach its own threshold. Unknown and disabled services must be handled before reading their counters. Some services already have failures before monitoring begins.

## Given

```python
services = {
    "auth": {"failure_count": 1, "threshold": 3, "enabled": True},
    "payments": {"failure_count": 0, "threshold": 2, "enabled": True},
    "search": {"failure_count": 0, "threshold": 2, "enabled": False}
}
events = [
    ("auth", "error"),
    ("payments", "timeout"),
    ("search", "error"),
    ("auth", "ok"),
    ("payments", "error"),
    ("payments", "error"),
    ("auth", "timeout"),
    ("ghost", "error"),
    ("auth", "error"),
    ("search", "ok")
]
fail_statuses = {"error", "timeout"}
```

## Requirements

1. Process `events` sequentially with a `while` loop, keeping their order.
2. For each event, classify it using this priority:
   - Service not found in `services` → count one **unknown event**, do nothing else.
   - Service exists but `enabled` is `False` → count one **disabled event**, do nothing else.
   - Status is in `fail_statuses` → increment that service's `failure_count` and increment **counted failures**.
   - Otherwise → count one **healthy event**, with no counter change.
3. If an enabled service reaches or exceeds its `threshold` after a counted failure and has not previously triggered an alert, print `ALERT: service at event N` and add that service to an alert set.
4. A service should trigger **at most one** alert even if further failure events arrive. Do not reset failure counts.
5. Don't mutate the original `events` list or its tuples. You may update the service counters in `services`.
6. Print: processed events, counted failures, disabled events, unknown events, healthy events, number of alerts, and alphabetically sorted alert service names.
7. Print final failure counts for `auth`, `payments`, `search` from the updated dictionary.
8. Ensure the five event categories (counted failures, disabled, unknown, healthy) add up to total processed events.

## Expected Output

```text
ALERT: payments at event 5
ALERT: auth at event 7

Processed: 10
Counted Failures: 6
Disabled Events: 2
Unknown Events: 1
Healthy Events: 1
Alerts Raised: 2
Alert Services: ['auth', 'payments']
Final Failures: auth=4, payments=3, search=0
```

## Constraints

- No `for`, comprehensions, custom functions, imports, or exception handling.
- Use membership to guard dictionary access for unknown services.
- An existing failure count may be nonzero; don't overwrite it with zero.
- Don't hardcode service alert decisions, counters, or event positions.

## My Approach

<!-- Explain your approach in your own words AFTER attempting the problem. -->

## Solutions

- [Solution 1](solution_1.py) — My independent attempt.
- Add `[Solution 2](solution_2.py)` if you find a genuinely different approach.

## What I Learned

<!-- Record mistakes, edge cases, and improvements after solving. -->
