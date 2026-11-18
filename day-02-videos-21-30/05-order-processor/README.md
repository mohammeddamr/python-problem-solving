# E-commerce Order Processor

**Difficulty:** Challenging  
**Topics:** Nested dictionaries, lists, strings, arithmetic, number formatting  
**Status:** Not solved

## Problem

Read a nested e-commerce order structure and generate an invoice using the quantities and prices inside the dictionary.

## Given

```python
order = {
    "id": "ord-0048",
    "customer": {
        "name": "  mONA   aLI ",
        "country": "EG"
    },
    "items": {
        "keyboard": {
            "price": 825.0,
            "qty": 2
        },
        "mouse": {
            "price": 230.0,
            "qty": 3
        }
    },
    "shipping": 65,
    "discount_pct": 10,
    "vat_pct": 14,
    "tags": ["new", "priority"]
}
```

## Requirements

1. Extract and uppercase the order ID.
2. Normalize the customer name to `Mona Ali`, with one space between the names.
3. Read each product price and quantity directly from the nested dictionary.
4. Calculate the combined subtotal.
5. Calculate a 10% discount from the subtotal.
6. Add shipping, then calculate 14% VAT on the discounted subtotal **plus shipping**.
7. Calculate the final total.
8. Append `reviewed` to the existing tags list.
9. Display a formatted invoice using two decimal places for currency.

## Expected output

```text
========== ORDER ==========
Order ID: ORD-0048
Customer: Mona Ali
Country: EG

Keyboard: 2 x EGP 825.00
Mouse: 3 x EGP 230.00

Subtotal: EGP 2,340.00
Discount: EGP 234.00
Shipping: EGP 65.00
VAT: EGP 303.94

FINAL TOTAL: EGP 2,474.94

Tags: ['new', 'priority', 'reviewed']
===========================
```

## Constraints

No loops, conditions, or custom functions. The input has exactly the two named products shown; read values from `order`, not duplicate constants in separate product variables. Do not hardcode final calculations.

## Extra challenge

What changes if you calculate VAT before adding shipping? Explain which formula this problem explicitly requests.

## My approach

_To fill in after solving: What approach did I choose, and why?_

## Solutions

| Solution | Technique | Notes |
| --- | --- | --- |
| [Solution 1](solution_1.py) | _To fill in_ | _To fill in_ |

> If you develop a genuinely different approach, create `solution_2.py` and add it to this table.

## What I learned

_To fill in: concepts reinforced, mistakes corrected, edge cases, and improvements._
