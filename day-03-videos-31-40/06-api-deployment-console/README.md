# API Deployment Console

**Day:** 03 · **Difficulty:** Challenging (Capstone)  
**Topics:** Nested dictionaries, tuples, lists, sets, input, comparisons, booleans, arithmetic, formatting

## Problem Description

You are preparing a backend service for release. Combine configuration parsing, a route audit, operator approval, capacity reservation, and server uptime in one CLI report — without using control flow from later videos.

## Given

```python
deployment = {
    "service": {"name": "  PAYMENTS--GATEWAY  ", "version": (3, 2, 1)},
    "routes": ["/pay", "/refund", "/pay", "/legacy"],
    "required": {"/pay", "/refund", "/health"},
    "deprecated": {"/legacy"},
    "limits": {"capacity": "1500", "in_use": "985"}
}

# Also ask the operator for:
# Name, extra slots to reserve, uptime seconds, release approval (yes/no)
```

## Example User Input

Enter these values at the prompts, one per line:

```text
  mONA  aLI  
125
93784
yes
```

## Requirements

1. Normalize service name to `payments-gateway`.
2. Unpack the version tuple and print `major.minor.patch` without printing parentheses or commas.
3. Read and normalize the operator’s name, convert extra slots and uptime seconds to integers, and parse approval as a Boolean.
4. Compute original route count, unique route count, and `/pay` occurrence count.
5. Determine required routes missing from the current routes, and deployed routes that are deprecated.
6. Make a new set of final routes with deprecated routes removed and missing required routes added (do not alter the input `routes` list).
7. Print the final routes sorted alphabetically as a List.
8. Convert the capacity and in-use strings to integers; reserve the requested extra slots and compute remaining capacity.
9. Calculate uptime as days, hours, minutes, seconds with padded `HH:MM:SS`.
10. Compute `routes_ready`: all required routes included in final routes AND final routes disjoint from deprecated routes.
11. Compute `capacity_ok`: projected usage does not exceed capacity and extra slots are positive.
12. Compute `runtime_ok`: uptime is at least 86,400 seconds.
13. Compute `deploy_ready`: operator approved AND routes ready AND capacity OK AND runtime OK.

## Expected Output

```text
Service: payments-gateway
Version: 3.2.1
Operator: Mona Ali
Original Route Count: 4
Unique Route Count: 3
/pay Occurrences: 2
Missing: {'/health'}
Deprecated: {'/legacy'}
Final Routes: ['/health', '/pay', '/refund']
Uptime: 1 days, 02:03:04
Capacity: 1500
Projected Usage: 1110
Remaining Capacity: 390
Approved: True
Routes Ready: True
Capacity OK: True
Runtime OK: True
Deploy Ready: True
```

## Constraints

- No `if` / ternary, loops, comprehensions, imports, custom functions, or `in` / `not in`.
- Do not use fixed slicing offsets or fixed output values.
- The provided data has the declared structure; input type errors need not be handled yet.
- Order is unspecified for arbitrary Sets; use sorting only for the final routes list.

## My Approach

<!-- Write your reasoning here AFTER attempting the problem. -->

## Solutions

- [Solution 1](solution_1.py) — My first independent implementation.
- Add `[Solution 2](solution_2.py)` if you create a distinct approach.

## What I Learned

<!-- Record mistakes, trade-offs, and lessons here. -->
