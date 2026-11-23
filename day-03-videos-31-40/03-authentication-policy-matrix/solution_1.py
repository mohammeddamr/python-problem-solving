"""Authentication Policy Matrix

Day 03 | Videos 31–40
First independent solution. No completed solution included.
See README.md for requirements and example output.
"""

accounts = {
    "primary": {
        "username": "dev01", "verified": True, "mfa": False,
        "locked": False, "failed_attempts": 2, "credits": "150"
    },
    "backup": {
        "username": "ops02", "verified": False, "mfa": True,
        "locked": False, "failed_attempts": 1, "credits": "850"
    }
}

policy = {
    "max_failed_attempts": 3,
    "min_billing_credits": 200,
    "allow_verified_without_mfa": True
}

# TODO: Extract and convert the necessary values for both accounts.
# TODO: Express the three policy flags for each account.
# TODO: Compute allowed login count without loops; print your results.
