# Subscription Age & Storage Meter

**Day:** 03 · **Difficulty:** Challenging  
**Topics:** User input, numeric conversion, approximate age calculations, `+=`, Booleans, formatting

## Problem Description

A storage service quotes a prepaid subscription using the customer’s age, usage, and renewal schedule. The service applies a simulated upload of 5.25 GB; update the usage in place.

## Given

```python
# Prompt for:
# Age in years (int)
# Storage quota in GB (float)
# Storage used in GB (float)
# Number of prepaid renewal months (int)
# Price per month in EGP (float)

upload_size_gb = 5.25
discount_percentage = 10
```

## Example User Input

Enter these values at the prompts, one per line:

```text
23
120.5
87.75
3
19.99
```

## Requirements

1. Read and convert all five user inputs; use `int()` and `float()` appropriately.
2. Calculate approximate age in months, days, complete weeks, hours, and minutes. Assume 365 days per year and 12 months per year (ignore leap years).
3. Calculate current percentage of the storage quota consumed.
4. Apply one additional 5.25 GB upload **using `+=`** to the `used_storage_gb` variable.
5. Recalculate percentage used and capacity remaining after the upload.
6. Calculate the total prepaid charge for renewal months with a fixed 10% discount.
7. Compute `eligible`: `18 <= age < 65` AND at least one renewal month AND remaining capacity at least zero.
8. Compute `near_limit`: updated used capacity is at least 80% of storage quota.
9. Print all values; show percentages and EGP prices with exactly two decimal places.

## Expected Output

```text
Age Months: 276
Age Days (approx): 8395
Full Weeks (approx): 1199
Age Hours (approx): 201480
Age Minutes (approx): 12088800

Usage Before: 72.82%
Usage After: 77.18%
Remaining Storage: 27.50 GB
Renewal Total (after discount): EGP 53.97
Eligible: True
Near Limit: False
```

## Constraints

- Assume age and quotas are positive, and the input includes the correct type of value.
- No `if`, loops, custom functions, comprehensions, imports, or membership operators.
- Compute using the user inputs, not the example values as constants.

## My Approach

<!-- Write your reasoning here AFTER attempting the problem. -->

## Solutions

- [Solution 1](solution_1.py) — My first independent implementation.
- Add `[Solution 2](solution_2.py)` if you create a distinct approach.

## What I Learned

<!-- Record mistakes, trade-offs, and lessons here. -->
