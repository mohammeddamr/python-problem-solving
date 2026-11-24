# Account Migration Auditor

**Day:** 04 · **Difficulty:** Hard  
**Topics:** while, string methods, membership, sets, dictionaries, data validation

## Problem Description

You are migrating old user records into a new system. Normalize emails and roles, reject invalid records with a clear reason, and never create duplicate migrated accounts. The order of checks matters: avoid indexing a missing email segment.

## Given

```python
raw_accounts = [
    {"email": "  Mona.ALI@Example.COM ", "role": "Admin", "active": True},
    {"email": "omar@example.com", "role": "member", "active": True},
    {"email": "mona.ali@example.com", "role": "admin", "active": True},
    {"email": "guest@unsafe.net", "role": "member", "active": True},
    {"email": "noura@example.com", "role": "EDITOR", "active": False},
    {"email": " yusuf@example.com ", "role": "Editor", "active": True},
    {"email": "bad-email", "role": "admin", "active": True}
]
allowed_domains = {"example.com", "company.org"}
allowed_roles = {"admin", "editor", "member"}
```

## Requirements

1. Process every account using `while`, preserving the input order.
2. Normalize an email by removing surrounding whitespace and lowercasing it; normalize the role similarly.
3. Apply these checks **in order**, stopping at the first failing rule for each record:
   - Email must contain exactly one `@` and have a nonempty part before and after it (`BAD_EMAIL`).
   - Domain after `@` must be in `allowed_domains` (`UNSUPPORTED_DOMAIN`).
   - Role must be in `allowed_roles` (`INVALID_ROLE`).
   - `active` must be `True` (`INACTIVE`).
   - Email must not already be in the set of **successfully migrated** accounts (`DUPLICATE`).
   - Otherwise: `MIGRATED`.
4. Print one line per input record in the form `01 | mona.ali@example.com | MIGRATED` or `03 | mona.ali@example.com | DUPLICATE`.
5. Maintain a set of migrated emails and a list preserving their migration order.
6. Print migrated/rejected counts, the ordered list, and the number of distinct migrated users.
7. Do not change the original `raw_accounts` records.

## Expected Output

```text
01 | mona.ali@example.com | MIGRATED
02 | omar@example.com | MIGRATED
03 | mona.ali@example.com | DUPLICATE
04 | guest@unsafe.net | UNSUPPORTED_DOMAIN
05 | noura@example.com | INACTIVE
06 | yusuf@example.com | MIGRATED
07 | bad-email | BAD_EMAIL

Migrated: 3
Rejected: 4
Migrated Emails: ['mona.ali@example.com', 'omar@example.com', 'yusuf@example.com']
Distinct Migrated: 3
```

## Constraints

- No `for`, comprehensions, functions, imports, regex, or exception handling.
- The `@` validation must happen before extracting the domain.
- Don't assume every email is valid or that rejected emails count as migrated.

## My Approach

<!-- Explain your approach in your own words AFTER attempting the problem. -->

## Solutions

- [Solution 1](solution_1.py) — My independent attempt.
- Add `[Solution 2](solution_2.py)` if you find a genuinely different approach.

## What I Learned

<!-- Record mistakes, edge cases, and improvements after solving. -->
