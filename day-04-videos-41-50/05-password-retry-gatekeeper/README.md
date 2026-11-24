# Password Retry Gatekeeper

**Day:** 04 · **Difficulty:** Challenging  
**Topics:** interactive while, nested conditions, dictionaries, short-circuit logic, loop termination

## Problem Description

Implement a small credential-checking console that allows a maximum of three attempts. The password and one-time code must both match exactly, with no accidental acceptance of partial or wrong values. Account existence and lock status are checked first.

## Given

```python
accounts = {
    "mona": {"password": "Key#2026", "otp": "8142", "locked": False},
    "omar": {"password": "Node!123", "otp": "9900", "locked": True}
}
max_attempts = 3

username_raw = input("Username: ")
# Ask for a password and one-time code inside your loop only when allowed.
```

## Requirements

1. Normalize the username with `strip().lower()`.
2. If the username is unknown, print `UNKNOWN ACCOUNT` and finish without asking for a password.
3. If the account is locked, print `ACCOUNT LOCKED` and finish without asking for a password.
4. Otherwise prompt `Password: ` and `OTP: ` for each attempt, with a maximum of `max_attempts`.
5. Authentication succeeds only when **both** entered values match the account's stored values exactly (case-sensitive).
6. After each failed attempt print `FAILED ATTEMPT N`, where N is the 1-based attempt count.
7. End the loop immediately **by making the loop condition false** on success; do not require `break` (taught after video 50).
8. On successful login print `ACCESS GRANTED`. If all attempts fail, print `ACCESS DENIED`.
9. Always print `Attempts Used: N` and `Attempts Remaining: N` for known, unlocked accounts.
10. The code must work for all successful-attempt positions and the all-failed case without changing the logic.

## Expected Output

Example 1 — Input sequence:

```text
mona
wrong
8142
Key#2026
0000
Key#2026
8142
```

Expected response lines (prompts omitted):

```text
FAILED ATTEMPT 1
FAILED ATTEMPT 2
ACCESS GRANTED
Attempts Used: 3
Attempts Remaining: 0
```

Example 2 — With username `omar`, expected output is just:

```text
ACCOUNT LOCKED
```

## Constraints

- Use `while` and `if` conditions; no custom functions, imports, `for`, exception handling, or `break` required.
- Credential strings are compared exactly; don't lowercase passwords or OTPs.
- Don't ask for another password once authentication succeeds.
- The limits must depend on `max_attempts`, not on hardcoded 3s inside your loop.

## My Approach

<!-- Explain your approach in your own words AFTER attempting the problem. -->

## Solutions

- [Solution 1](solution_1.py) — My independent attempt.
- Add `[Solution 2](solution_2.py)` if you find a genuinely different approach.

## What I Learned

<!-- Record mistakes, edge cases, and improvements after solving. -->
