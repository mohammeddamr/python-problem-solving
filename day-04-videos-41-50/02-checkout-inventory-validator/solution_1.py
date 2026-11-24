"""Checkout & Inventory Validator | Day 04 | Videos 41–50.
Independent solution: see README.md. No finished solution included.
"""

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
# TODO: Validate each cart line in a while loop.
# TODO: Update remaining stock only for accepted lines.
# TODO: Apply tiered coupon and shipping conditions.
# TODO: Compute and print the invoice and stock report.
