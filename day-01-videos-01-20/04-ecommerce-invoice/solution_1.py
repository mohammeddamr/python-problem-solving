"""E-commerce Invoice Engine

Day 01 | Videos 1–20
First independent solution. No finished solution included.
"""

# ## Requirements

# 1. Calculate subtotal from both product totals.
# 2. Calculate a 12% subtotal discount and the discounted subtotal.
# 3. Add shipping.
# 4. Calculate 14% VAT from the discounted subtotal plus shipping.
# 5. Calculate and display the final total.

# ## Expected output

# ```text
# ========== INVOICE ==========
# Subtotal:      EGP 2,017.15
# Discount:      EGP 242.06
# Shipping:      EGP 75.00
# VAT:           EGP 259.01
# -----------------------------
# Final Total:   EGP 2,109.10
# =============================
# ```

product_a_price = 199.95
product_a_quantity = 7
product_b_price = 47.50
product_b_quantity = 13
discount_percentage = 12
shipping_fee = 75
vat_percentage = 14

# TODO: Implement your calculations 
subtotal=product_a_price*product_a_quantity + product_b_price *product_b_quantity 
discount=(discount_percentage/100)*subtotal
vat=(vat_percentage/100)*(subtotal-discount+shipping_fee)
total=subtotal-discount+shipping_fee+vat

paper=f"""
========== INVOICE ==========
Subtotal:      EGP {subtotal:,.2f}
Discount:      EGP {discount:,.2f}
Shipping:      EGP {shipping_fee:,.2f}
VAT:           EGP {vat:,.2f}
-----------------------------
Final Total:   EGP {total:,.2f}
=============================
"""
print(paper)