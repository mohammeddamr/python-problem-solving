"""Backend Ticket Queue Manager

Day 02 | Videos 21–30
First independent solution. No finished solution included.
"""

# ## Requirements

# 1. Save an independent copy of the original list as `original_tickets` before making any changes.
# 2. Remove surrounding whitespace from the first ticket.
# 3. Count how many times `auth_failed` appears **after cleaning the first ticket**, before removing a duplicate.
# 4. Remove exactly **one** occurrence of `auth_failed`.
# 5. Insert `security_alert` immediately **before** `db_down` without hardcoding the numeric index.
# 6. Remove `profile_updated` using `pop()` and store the removed value as `resolved_ticket`.
# 7. Sort the remaining tickets alphabetically.
# 8. Print the final queue and the unchanged original list.

# ## Expected output

# ```text
# AUTH FAILED COUNT: 2
# RESOLVED: profile_updated

# FINAL QUEUE:
# ['auth_failed', 'db_down', 'payment_timeout', 'security_alert']

# ORIGINAL QUEUE:
# ['  auth_failed  ', 'payment_timeout', 'auth_failed', 'profile_updated', 'db_down']
# ```

tickets = [
    "  auth_failed  ",
    "payment_timeout",
    "auth_failed",
    "profile_updated",
    "db_down"
]
# TODO: Implement your calculations and print the requested output.

original_tickets=tickets.copy()
tickets[0]=tickets[0].strip()
c=tickets.count("auth_failed")
tickets.remove("auth_failed")
i_db_down=tickets.index("db_down")
tickets.insert(i_db_down,"security_alert")
resolved_ticket=tickets.pop(tickets.index("profile_updated"))
tickets.sort()

print(f"""
# ```text
# AUTH FAILED COUNT: {c}
# RESOLVED: {resolved_ticket}

# FINAL QUEUE:
# {tickets}

# ORIGINAL QUEUE:
# {original_tickets}
# ```""")