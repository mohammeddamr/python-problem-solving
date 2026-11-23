"""Interactive Checkout Validator

Day 03 | Videos 31–40
First independent solution. No completed solution included.
See README.md for requirements and example output.
"""

# All values must come from input().
customer_name = input("Customer name: ")
unit_price_raw = input("Unit price (EGP): ")
quantity_raw = input("Quantity: ")
discount_raw = input("Discount percentage: ")
shipping_raw = input("Shipping fee (EGP): ")
paid_raw = input("Payment received (yes/no): ")

vat_percentage = 14

# TODO: Normalize and convert user inputs.
# TODO: Calculate invoice amounts and Boolean validity flags.
# TODO: Print the checkout report using the computed values.
