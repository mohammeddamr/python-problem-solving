"""Subscription Age & Storage Meter

Day 03 | Videos 31–40
First independent solution. No completed solution included.
See README.md for requirements and example output.
"""

# TODO: Convert input values to appropriate numeric types.
# TODO: Calculate all requested approximate age units.
# TODO: Compute usage before/after a simulated upload; use +=.
# TODO: Calculate prepaid cost, Boolean flags, and print results.

# ## Requirements

# 1. Read and convert all five user inputs; use `int()` and `float()` appropriately.
# 2. Calculate approximate age in months, days, complete weeks, hours, and minutes. Assume 365 days per year and 12 months per year (ignore leap years).
# 3. Calculate current percentage of the storage quota consumed.
# 4. Apply one additional 5.25 GB upload **using `+=`** to the `used_storage_gb` variable.
# 5. Recalculate percentage used and capacity remaining after the upload.
# 6. Calculate the total prepaid charge for renewal months with a fixed 10% discount.
# 7. Compute `eligible`: `18 <= age < 65` AND at least one renewal month AND remaining capacity at least zero.
# 8. Compute `near_limit`: updated used capacity is at least 80% of storage quota.
# 9. Print all values; show percentages and EGP prices with exactly two decimal places.

# ## Expected Output

# ```text
# Age Months: 276
# Age Days (approx): 8395
# Full Weeks (approx): 1199
# Age Hours (approx): 201480
# Age Minutes (approx): 12088800

# Usage Before: 72.82%
# Usage After: 77.18%
# Remaining Storage: 27.50 GB
# Renewal Total (after discount): EGP 53.97
# Eligible: True
# Near Limit: False
# ```


age_raw = input("Age in years: ")
quota_raw = input("Storage quota (GB): ")
used_raw = input("Storage used (GB): ")
renewals_raw = input("Prepaid renewal months: ")
monthly_price_raw = input("Price per month (EGP): ")

upload_size_gb = 5.25
discount_percentage = 10

age=int(age_raw)
quota=float(quota_raw)
used=float(used_raw)
renewals=float(renewals_raw)
monthly_price=float(monthly_price_raw)

age_months=age*12
age_days=age*365
age_weeks=(age*365)//7
age_hours=age*365*24
age_mins=age*365*24*60

current_percent=used/quota*100
used+=upload_size_gb
next_percent=used/quota*100
remaining=quota-used

total_price=renewals*monthly_price*(100-discount_percentage)/100
eligable= (18 <=age<65) and renewals>=1 and remaining>=0
near_limit= (next_percent) >=80

print(f"""
# ```text
# Age Months: {age_months}
# Age Days (approx): {age_days}
# Full Weeks (approx): {age_weeks}
# Age Hours (approx): {age_hours}
# Age Minutes (approx): {age_mins}

# Usage Before: {current_percent:.2f} %
# Usage After: {next_percent:.2f} %
# Remaining Storage: {remaining:.2f} GB
# Renewal Total (after discount): EGP {total_price:.2f}
# Eligible: {eligable}
# Near Limit: {near_limit}
# ```
""")