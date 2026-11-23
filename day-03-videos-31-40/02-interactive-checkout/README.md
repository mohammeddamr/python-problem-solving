# Interactive Checkout Validator

**Day:** 03 · **Difficulty:** Hard  
**Topics:** User input, type conversion, string cleanup, numeric formatting, Boolean logic

## Problem Description

Build a tiny command-line checkout screen. All supplied values come from `input()` as strings; convert and validate them using expressions, without any branches.

## Given

```python
# Your program must prompt for:
# Customer name
# Unit price (EGP)
# Quantity
# Discount percentage
# Shipping fee (EGP)
# Payment received (yes/no)
```

## Example User Input

Enter these values at the prompts, one per line:

```text
  sARa   aLi
249.90
6
12
65
yes
```

## Requirements

1. Read all six fields with `input()` (do not replace them with fixed constants).
2. Normalize the customer name to `Sara Ali` even though the sample contains extra spaces and inconsistent capitalization.
3. Convert quantities and money/percentage inputs to appropriate numeric types.
4. Compute subtotal, discount amount, discounted subtotal, then shipping.
5. Compute VAT = 14% of the discounted subtotal **plus shipping**.
6. Compute the final amount, preserving intermediate precision until display.
7. Create Boolean values: `valid_quantity` (`qty > 0`), `valid_discount` (`0 <= discount <= 100`), and `payment_received` (case-insensitive `yes`).
8. Create `ready_to_fulfill` as a logical AND of those three flags and a positive final amount.
9. Print money with comma grouping and exactly two decimal places.

## Expected Output

```text
CUSTOMER: Sara Ali
Subtotal: EGP 1,499.40
Discount: EGP 179.93
Shipping: EGP 65.00
VAT: EGP 193.83
TOTAL: EGP 1,578.30
Quantity Valid: True
Discount Valid: True
Payment Received: True
Ready to Fulfill: True
```

## Constraints

- Only the VAT rate (14%) is a predefined business constant.
- Assume the user enters values of the documented types; exception handling is not required.
- No if/else, loops, comprehensions, custom functions, or membership tests.

## My Approach

<!-- Write your reasoning here AFTER attempting the problem. -->

## Solutions

- [Solution 1](solution_1.py) — My first independent implementation.
- Add `[Solution 2](solution_2.py)` if you create a distinct approach.

## What I Learned

<!-- Record mistakes, trade-offs, and lessons here. -->
