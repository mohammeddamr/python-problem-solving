"""Production Deployment Auditor

Day 02 | Videos 21–30
First independent solution. No finished solution included.
"""

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
