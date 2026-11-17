"""Warehouse Packaging System

Day 01 | Videos 1–20
First independent solution. No finished solution included.
"""

# ## Requirements

# 1. Calculate the number of complete cartons.
# 2. Find units not sufficient for a complete carton.
# 3. Calculate the number of complete pallets.
# 4. Find the complete cartons remaining outside those pallets.
# 5. Calculate the total value of all complete cartons.

# ## Expected output

# ```text
# ========== WAREHOUSE ==========
# Total Units: 42,785
# Full Cartons: 1,782
# Remaining Units: 17

# Full Pallets: 31
# Remaining Cartons: 46

# Cartons Value: EGP 33,412.50
# ===============================
# ```

total_units = 42785
units_per_carton = 24
cartons_per_pallet = 56
price_per_full_carton = 18.75

full_cartons=total_units//units_per_carton
rem_units=total_units%units_per_carton

full_pallets=full_cartons//cartons_per_pallet
rem_cartons=full_cartons%cartons_per_pallet

cartons_value=full_cartons*price_per_full_carton

warehouse=f"""
========== WAREHOUSE ==========
Total Units: {total_units:,d}
Full Cartons: {full_cartons:,d}
Remaining Units: {rem_units:,d}

Full Pallets: {full_pallets:,d}
Remaining Cartons: {rem_cartons:,d}

Cartons Value: EGP {cartons_value:,.2f}
===============================
"""
print(warehouse)

# TODO: Implement your calculations and print the requested output.
