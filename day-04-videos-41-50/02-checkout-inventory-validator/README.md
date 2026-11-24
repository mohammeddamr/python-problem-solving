# Checkout & Inventory Validator

**Day:** 04 · **Difficulty:** Challenging  
**Topics:** while, nested dictionaries, lists, validation, arithmetic, formatting

## Problem Description

Build a small e-commerce checkout engine. A cart contains valid orders, invalid quantities, unavailable products, and a stock shortage. Accept or reject each line in sequence; accepted lines must consume stock so later lines see the **updated** stock. Calculate the final invoice from accepted lines only.

## Given

```python
catalog = {
    "keyboard": {"price": 850.0, "stock": 3},
    "mouse": {"price": 245.0, "stock": 10},
    "headset": {"price": 1190.0, "stock": 2}
}
cart = [
    {"product": "keyboard", "qty": 2},
    {"product": "mouse", "qty": 4},
    {"product": "headset", "qty": 3},
    {"product": "usb-cable", "qty": 1},
    {"product": "mouse", "qty": 0},
    {"product": "keyboard", "qty": 1}
]
coupon = "SAVE10"
valid_coupons = {"SAVE10", "VIP15"}
shipping_fee = 65
vat_pct = 14
```

## Requirements

1. Iterate over `cart` using `while` (do not use `for`).
2. For each line apply **priority**: unknown product → `UNKNOWN_PRODUCT`; non-positive quantity → `INVALID_QTY`; quantity exceeds **current remaining stock** → `OUT_OF_STOCK`; otherwise → `ACCEPTED`.
3. Display one status per cart line as `Line 1: ACCEPTED` or `Line 4: UNKNOWN_PRODUCT`.
4. For an accepted line: add `qty * price` to the subtotal and subtract `qty` from the corresponding product stock.
5. Count accepted and rejected lines; do not mutate the `cart` list.
6. A coupon provides a discount only when the subtotal is **at least EGP 2,500** and the coupon is valid: `SAVE10` = 10%, `VIP15` = 15%; otherwise 0%. Select the percentage via `if/elif/else`.
7. Shipping is free if the **discounted subtotal** is at least EGP 3,000; otherwise add `shipping_fee`.
8. Calculate VAT as `14%` of (discounted subtotal + actual shipping), then the final charge.
9. Display remaining stock for all three catalog items and print money to exactly 2 decimals.
10. Test changing quantities: when a prior line reserves stock, subsequent requests must respect the reduced stock.

## Expected Output

```text
Line 1: ACCEPTED
Line 2: ACCEPTED
Line 3: OUT_OF_STOCK
Line 4: UNKNOWN_PRODUCT
Line 5: INVALID_QTY
Line 6: ACCEPTED

Accepted Lines: 3
Rejected Lines: 3
Subtotal: EGP 3,530.00
Discount: EGP 353.00
Shipping: EGP 0.00
VAT: EGP 444.78
Final Charge: EGP 3,621.78
Stock Left: keyboard=0, mouse=6, headset=2
```

## Constraints

- No `for`, comprehensions, functions, imports, or exceptions.
- Work directly with the provided nested dictionaries and cart data.
- Use the **remaining** stock, not initial stock, for validation.
- Don't hardcode final prices or quantities.

## My Approach

<!-- Explain your approach in your own words AFTER attempting the problem. -->

## Solutions

- [Solution 1](solution_1.py) — My independent attempt.
- Add `[Solution 2](solution_2.py)` if you find a genuinely different approach.

## What I Learned

<!-- Record mistakes, edge cases, and improvements after solving. -->
