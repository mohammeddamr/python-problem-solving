"""Production Deployment Auditor

Day 02 | Videos 21–30
First independent solution. No finished solution included.
"""

# ## Requirements

# 1. Find services in both `live` and `approved`. intersection
# 2. Find unapproved services that are currently live. live w msh f approved
# 3. Find approved services missing from production.
# 4. Find services that occur in exactly one of those two sets. mawgowda fy el etnen 
# 5. Find currently live services listed as disabled.
# 6. Check whether all critical services are live using an appropriate set comparison method.
# 7. Check whether all critical services are approved.
# 8. Create `fixed_live` as an independent copy of `live`, remove unapproved services, and add missing approved services using set update methods.
# 9. Check that `fixed_live` contains every approved service and has no disabled service.
# 10. Print the results and Boolean checks.

# ## Expected output

# ```text
# DEPLOYMENT AUDIT
# Common: {'auth', 'payments', 'notifications'}
# Unapproved: {'search', 'legacy'}
# Missing: {'analytics'}
# Different: {'search', 'legacy', 'analytics'}
# Running disabled: {'legacy'}
# All critical live?: True
# Approved covers critical?: True
# Fixed covers approved?: True
# Fixed avoids disabled?: True
# ```


live = {
    "auth", "payments", "search",
    "notifications", "legacy"
}

approved = {
    "auth", "payments",
    "analytics", "notifications"
}

critical = {"auth", "payments"}

disabled = {"legacy", "old_admin"}

# TODO: Implement your calculations and print the requested output.


common=live.intersection(approved)
unapproved_live=live.difference(approved)
approved_unlive=approved.difference(live)
Different=approved.symmetric_difference(live)
running_disabled=live.intersection(disabled)
is_live=critical.issubset(live)
is_approved=critical.issubset(approved)

fixed_live=live.copy()
fixed_live.intersection_update(approved)
fixed_live.update(approved)
fis_approved=approved.issubset(fixed_live)
fisnot_disabled=fixed_live.isdisjoint(disabled)

print(f"""
# DEPLOYMENT AUDIT
# Common: {common}
# Unapproved: {unapproved_live}
# Missing: {approved_unlive}
# Different: {Different}
# Running disabled: {running_disabled}
# All critical live?: {is_live}
# Approved covers critical?: {is_approved}
# Fixed covers approved?: {fis_approved}
# Fixed avoids disabled?: {fisnot_disabled}
 """)