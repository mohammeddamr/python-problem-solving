# Authentication Policy Matrix

**Day:** 03 · **Difficulty:** Challenging  
**Topics:** Nested dictionaries, Booleans, `and`/`or`/`not`, comparisons, numeric conversion

## Problem Description

An authentication service evaluates two stored account records. You must express the policy using Boolean expressions — no conditional statements.

## Given

```python
accounts = {
    "primary": {
        "username": "dev01", "verified": True, "mfa": False,
        "locked": False, "failed_attempts": 2, "credits": "150"
    },
    "backup": {
        "username": "ops02", "verified": False, "mfa": True,
        "locked": False, "failed_attempts": 1, "credits": "850"
    }
}

policy = {
    "max_failed_attempts": 3,
    "min_billing_credits": 200,
    "allow_verified_without_mfa": True
}
```

## Requirements

1. Convert each account’s `credits` string to an integer; retain the original account data unchanged.
2. For EACH account compute `login_allowed`: verified AND not locked AND failed attempts below maximum AND (MFA enabled OR policy permits verified accounts without MFA).
3. For EACH account compute `billing_allowed`: login allowed AND numeric credits greater than or equal to required billing credits.
4. For EACH account compute `needs_review`: locked OR attempts at/above the maximum OR not verified.
5. Count how many accounts have `login_allowed == True` without loops (there are exactly two named accounts).
6. Print the three flags per account and total permitted logins.
7. Use meaningful parentheses: the policy must not silently change due to Boolean precedence.

## Expected Output

```text
PRIMARY (dev01)
Login Allowed: True
Billing Allowed: False
Needs Review: False

BACKUP (ops02)
Login Allowed: False
Billing Allowed: False
Needs Review: True

Allowed Login Count: 1
```

## Constraints

- Do not use `if`, ternary operators, loops, custom functions, or membership operators.
- No hardcoded eligibility answers.
- Do not use string comparisons for numeric credits.

## My Approach

<!-- Write your reasoning here AFTER attempting the problem. -->

## Solutions

- [Solution 1](solution_1.py) — My first independent implementation.
- Add `[Solution 2](solution_2.py)` if you create a distinct approach.

## What I Learned

<!-- Record mistakes, trade-offs, and lessons here. -->
