# Production Deployment Auditor

**Difficulty:** Challenging  
**Topics:** Set operations, subset/superset, disjointness, set updates, copying  
**Status:** Not solved

## Problem

Compare deployed services with approved services, identify problems, then prepare a corrected deployment set.

## Given

```python
live = {
    "auth", "payments", "search",
    "notifications", "legacy"
}

approved = {
    "auth", "payments",
    "analytics", "notifications"
}

critical = {"auth", "payments"}

disabled = {"legacy", "old_admin"}
```

## Requirements

1. Find services in both `live` and `approved`.
2. Find unapproved services that are currently live.
3. Find approved services missing from production.
4. Find services that occur in exactly one of those two sets.
5. Find currently live services listed as disabled.
6. Check whether all critical services are live using an appropriate set comparison method.
7. Check whether all critical services are approved.
8. Create `fixed_live` as an independent copy of `live`, remove unapproved services, and add missing approved services using set update methods.
9. Check that `fixed_live` contains every approved service and has no disabled service.
10. Print the results and Boolean checks.

## Expected output

```text
DEPLOYMENT AUDIT
Common: {'auth', 'payments', 'notifications'}
Unapproved: {'search', 'legacy'}
Missing: {'analytics'}
Different: {'search', 'legacy', 'analytics'}
Running disabled: {'legacy'}
All critical live?: True
Approved covers critical?: True
Fixed covers approved?: True
Fixed avoids disabled?: True
```

## Constraints

Set display order may vary. Do not change `live` itself. Use set methods/operators only from videos 26–29; no loops, conditions, or custom functions.

## Extra challenge

Explain the difference between `difference()` and `difference_update()`, and why their return values differ.

## My approach

_To fill in after solving: What approach did I choose, and why?_

## Solutions

| Solution | Technique | Notes |
| --- | --- | --- |
| [Solution 1](solution_1.py) | _To fill in_ | _To fill in_ |

> If you develop a genuinely different approach, create `solution_2.py` and add it to this table.

## What I learned

_To fill in: concepts reinforced, mistakes corrected, edge cases, and improvements._
