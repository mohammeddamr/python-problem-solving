# Email Alias Verification Parser

**Day:** 03 · **Difficulty:** Hard  
**Topics:** `input()`, `find()`, slicing, string methods, comparison and Boolean operators

## Problem Description

A registration platform accepts tagged email aliases such as `name+tag@domain`. Parse every component with dynamic string boundaries, validate it, and mask the base mailbox name.

## Given

```python
raw_email = input("Tagged email: ")
```

## Example User Input

Enter these values at the prompts, one per line:

```text
  NOra.DeV+OPS@Example.COM  
```

## Requirements

1. Read a tagged address from the user, strip surrounding whitespace, and lowercase it.
2. Find the position of `+` and `@` dynamically with `find()` (no hardcoded character offsets).
3. Extract three parts: `base_username`, `alias_tag`, and `domain`.
4. Generate `masked_email`: keep the first two and last two characters of the base username, mask its middle with `*`, then retain the `+tag@domain` suffix.
5. Compute `single_at`: the normalized input contains exactly one `@`.
6. Compute `trusted_domain`: domain equals `example.com` OR `company.org`.
7. Compute `valid_alias`: base username has at least 6 characters AND alias tag at least 2 characters AND `single_at` AND `trusted_domain`.
8. Display the normalized email, all parsed fields, masked email, and Boolean flags.

## Expected Output

```text
Normalized: nora.dev+ops@example.com
Base Username: nora.dev
Alias: ops
Domain: example.com
Masked: no****ev+ops@example.com
Single @: True
Trusted Domain: True
Valid Alias: True
```

## Constraints

- The input format is guaranteed to contain one `+` before one `@` and at least four characters in its base username; you are checking its policy validity, not building a fault-tolerant parser.
- Use `find()` and slicing for extraction, not hardcoded positions.
- Use `len()` and string multiplication for dynamic masking.
- No `if`, loops, custom functions, or membership operators.

## My Approach

<!-- Write your reasoning here AFTER attempting the problem. -->

## Solutions

- [Solution 1](solution_1.py) — My first independent implementation.
- Add `[Solution 2](solution_2.py)` if you create a distinct approach.

## What I Learned

<!-- Record mistakes, trade-offs, and lessons here. -->
