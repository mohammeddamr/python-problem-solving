# Login Risk Triage Queue

**Day:** 04 · **Difficulty:** Hard  
**Topics:** `while`, nested `if/elif/else`, dictionaries, sets, membership, counters

## Problem Description

You're implementing a small authentication log triage engine. Events must be examined in their original order and assigned exactly one decision. Your engine must follow **priority rules**, not just independently evaluate all conditions. Summarize outcomes and unique denied usernames.

## Given

```python
accounts = {
    "mona": {"locked": False, "mfa_required": True},
    "omar": {"locked": False, "mfa_required": False},
    "ali": {"locked": False, "mfa_required": True},
    "sara": {"locked": False, "mfa_required": True},
    "root": {"locked": True, "mfa_required": True}
}
trusted_ips = {"10.0.0.10", "10.0.0.20"}
events = [
    {"user": "mona", "ip": "10.0.0.10", "password_ok": True, "mfa_ok": True},
    {"user": "omar", "ip": "10.0.0.20", "password_ok": True, "mfa_ok": False},
    {"user": "guest", "ip": "10.0.0.30", "password_ok": True, "mfa_ok": True},
    {"user": "ali", "ip": "10.0.0.99", "password_ok": True, "mfa_ok": True},
    {"user": "sara", "ip": "10.0.0.10", "password_ok": False, "mfa_ok": True},
    {"user": "omar", "ip": "10.0.0.20", "password_ok": True, "mfa_ok": True},
    {"user": "root", "ip": "10.0.0.10", "password_ok": True, "mfa_ok": True},
    {"user": "mona", "ip": "10.0.0.10", "password_ok": True, "mfa_ok": False}
]
```

## Requirements

1. Read `events` using a `while` loop and an index, **without** using a `for` loop.
2. For each event, determine one decision according to this **strict first-match priority**:
   - `unknown_user`: username is not a key in `accounts`.
   - `locked`: account exists but its `locked` field is `True`.
   - `untrusted_ip`: event IP is not in `trusted_ips`.
   - `invalid_password`: password check failed.
   - `mfa_missing`: the account requires MFA but MFA check failed.
   - Otherwise: `APPROVED`.
3. Every event must produce a line in this format: `01 | mona | APPROVED` or `03 | guest | DENIED: unknown_user`. Use a two-digit event number.
4. Count approved and denied events separately.
5. Store distinct denied usernames in a `set` and print them as an alphabetically sorted `list`.
6. Do not mutate any of the given input data structures.
7. Test changing account rules and adding events without changing the processing logic.

## Expected Output

```text
01 | mona | APPROVED
02 | omar | APPROVED
03 | guest | DENIED: unknown_user
04 | ali | DENIED: untrusted_ip
05 | sara | DENIED: invalid_password
06 | omar | APPROVED
07 | root | DENIED: locked
08 | mona | DENIED: mfa_missing

Approved: 3
Denied: 5
Unique Denied Users: ['ali', 'guest', 'mona', 'root', 'sara']
```

## Constraints

- Use only concepts from lessons 1–50: no `for`, comprehensions, custom functions, imports, or exception handling.
- Use conditional branching and membership checks. No hardcoded final decisions.
- The event list can become longer; your loop must still process every event.

## My Approach

<!-- Explain your approach in your own words AFTER attempting the problem. -->

## Solutions

- [Solution 1](solution_1.py) — My independent attempt.
- Add `[Solution 2](solution_2.py)` if you find a genuinely different approach.

## What I Learned

<!-- Record mistakes, edge cases, and improvements after solving. -->
