"""Interactive Checkout Validator

Day 03 | Videos 31–40
First independent solution. No completed solution included.
See README.md for requirements and example output.
"""

# 1. Read all six fields with `input()` (do not replace them with fixed constants).
# 2. Normalize the customer name to `Sara Ali` even though the sample contains extra spaces and inconsistent capitalization.
# 3. Convert quantities and money/percentage inputs to appropriate numeric types.
# 4. Compute subtotal, discount amount, discounted subtotal, then shipping.
# 5. Compute VAT = 14% of the discounted subtotal **plus shipping**.
# 6. Compute the final amount, preserving intermediate precision until display.
# 7. Create Boolean values: `valid_quantity` (`qty > 0`), `valid_discount` (`0 <= discount <= 100`), and `payment_received` (case-insensitive `yes`).
# 8. Create `ready_to_fulfill` as a logical AND of those three flags and a positive final amount.
# 9. Print money with comma grouping and exactly two decimal places.

# ## Expected Output

# ```text
# CUSTOMER: Sara Ali
# Subtotal: EGP 1,499.40
# Discount: EGP 179.93
# Shipping: EGP 65.00
# VAT: EGP 193.83
# TOTAL: EGP 1,578.30
# Quantity Valid: True
# Discount Valid: True
# Payment Received: True
# Ready to Fulfill: True
# ```

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

customer_name=" ".join(customer_name.strip().lower().split()).title()
unit_price_raw=float(unit_price_raw)
quantity_raw=float(quantity_raw)
discount_raw=float(discount_raw)
shipping_raw=float(shipping_raw)
paid_raw=paid_raw.lower()
subtotal=unit_price_raw*quantity_raw
discount=(discount_raw/100)*subtotal
vat=(vat_percentage/100)*(subtotal-discount+shipping_raw)
total=subtotal-discount+shipping_raw+vat
valid_quantity=quantity_raw>0
valid_discount=0<=discount_raw<=100
payment_received= (paid_raw == "yes")
ready_to_fulfill=(total>0) and payment_received and valid_discount and valid_quantity

print(f"""

# ```text
# CUSTOMER: {customer_name}
# Subtotal: EGP {subtotal:,.2f}
# Discount: EGP {discount:,.2f}
# Shipping: EGP {shipping_raw:,.2f}
# VAT: EGP {vat:,.2f}
# TOTAL: EGP {total:,.2f}
# Quantity Valid: {valid_quantity}
# Discount Valid: {valid_discount}
# Payment Received: {payment_received}
# Ready to Fulfill: {ready_to_fulfill}
# ```
 """)