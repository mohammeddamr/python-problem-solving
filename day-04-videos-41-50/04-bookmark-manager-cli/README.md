# Interactive Bookmark Manager CLI

**Day:** 04 · **Difficulty:** Challenging  
**Topics:** while loop, input, if/elif/else, list methods, string validation, membership

## Problem Description

Implement a console bookmarks manager, inspired by the course's bookmarks training. The user may issue multiple commands until choosing `quit`. Handle malformed URLs, duplicates, and missing entries without exceptions.

## Given

```python
bookmarks = ["https://docs.python.org", "https://github.com"]

# Commands to support: add, remove, check, list, quit.
# Use input() to read the command; ask for a URL on add/remove/check.
```

## Requirements

1. Repeatedly ask `Command: ` and normalize command input using `strip().lower()`.
2. Implement `add`, `remove`, `check`, `list`, and `quit` with `while` and `if/elif/else`.
3. For `add`, `remove`, or `check`, ask for a `URL: ` and remove surrounding spaces.
4. `add`: accept only a nonempty HTTPS URL with **at least one character after** `https://`; report `INVALID URL` otherwise. If already saved, say `ALREADY SAVED`; else append and say `ADDED`.
5. `remove`: remove an existing exact URL with `remove()` and print `REMOVED`; otherwise print `NOT FOUND`.
6. `check`: say `FOUND` when URL is an exact member, else `NOT FOUND`.
7. `list`: print an **alphabetically sorted copy** of the bookmarks, without reordering the stored list.
8. Any other command except `quit` should print `UNKNOWN COMMAND` without terminating.
9. On `quit`, print `GOODBYE` followed by final saved count and the number of **successful** additions and removals.
10. The loop must terminate on `quit` without using `for` or a custom function.

## Expected Output

Input sequence (one line per prompt):

```text
add
https://fastapi.tiangolo.com
add
https://github.com
add
ftp://internal
check
https://docs.python.org
remove
https://github.com
remove
https://missing.dev
list
quit
```

Expected response lines (input prompts omitted):

```text
ADDED
ALREADY SAVED
INVALID URL
FOUND
REMOVED
NOT FOUND
['https://docs.python.org', 'https://fastapi.tiangolo.com']
GOODBYE
Saved: 2
Successful Adds: 1
Successful Removes: 1
```

## Constraints

- Interactive `input()` + `while` required; no `for`, custom functions, imports, or exceptions.
- Use membership to guard `remove()` so a missing URL does not crash the program.
- Only successful changes count toward addition/removal totals.
- Test repeated commands, blank commands, extra spaces, and an immediate `quit`.

## My Approach

<!-- Explain your approach in your own words AFTER attempting the problem. -->

## Solutions

- [Solution 1](solution_1.py) — My independent attempt.
- Add `[Solution 2](solution_2.py)` if you find a genuinely different approach.

## What I Learned

<!-- Record mistakes, edge cases, and improvements after solving. -->
