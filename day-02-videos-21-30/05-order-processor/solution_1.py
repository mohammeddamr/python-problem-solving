"""E-commerce Order Processor

Day 02 | Videos 21–30
First independent solution. No finished solution included.
"""
# ## Requirements

# 1. Extract and uppercase the order ID.
# 2. Normalize the customer name to `Mona Ali`, with one space between the names.
# 3. Read each product price and quantity directly from the nested dictionary.
# 4. Calculate the combined subtotal.
# 5. Calculate a 10% discount from the subtotal.
# 6. Add shipping, then calculate 14% VAT on the discounted subtotal **plus shipping**.
# 7. Calculate the final total.
# 8. Append `reviewed` to the existing tags list.
# 9. Display a formatted invoice using two decimal places for currency.

# ## Expected output

# ```text
# ========== ORDER ==========
# Order ID: ORD-0048
# Customer: Mona Ali
# Country: EG

# Keyboard: 2 x EGP 825.00
# Mouse: 3 x EGP 230.00

# Subtotal: EGP 2,340.00
# Discount: EGP 234.00
# Shipping: EGP 65.00
# VAT: EGP 303.94

# FINAL TOTAL: EGP 2,474.94

# Tags: ['new', 'priority', 'reviewed']
# ===========================
# ```

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
# TODO: Implement your calculations and print the requested output.
order_id=order["id"].upper()
name=order["customer"]["name"].split()
name=" ".join(name).title()
kp=order["items"]["keyboard"]["price"]
mp=order["items"]["mouse"]["price"]
mq=order["items"]["mouse"]["qty"]
kq=order["items"]["keyboard"]["qty"]

shipping=order["shipping"]
discount=order["discount_pct"]/100
vat=order["vat_pct"]/100
subtotal=kq*kp+mq*mp
VAT=(subtotal+shipping-(subtotal*discount))*vat
total=subtotal+VAT+shipping-(subtotal*discount)
order["tags"].append("reviewed")

print(f"""
      
# ========== ORDER ==========
# Order ID: {order_id}
# Customer: {name}
# Country: {order["customer"]["country"]}

# Keyboard: {kq} x EGP {kp:.2f}
# Mouse: {mq} x EGP {mp:.2f}

# subtotal: EGP {subtotal:,.2f}
# Discount: EGP {(subtotal)*discount:.2f}
# Shipping: EGP {shipping}
# VAT: EGP {VAT:.2f}

# FINAL TOTAL: EGP {total:,.2f}

# Tags: {order["tags"]}
# ===========================
      """)