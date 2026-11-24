"""Password Retry Gatekeeper | Day 04 | Videos 41–50.
Independent solution: see README.md. No finished solution included.
"""

accounts = {
    "mona": {"password": "Key#2026", "otp": "8142", "locked": False},
    "omar": {"password": "Node!123", "otp": "9900", "locked": True}
}
max_attempts = 3

username_raw = input("Username: ")
# Ask for a password and one-time code inside your loop only when allowed.
# TODO: Validate the account before prompting for credentials.
# TODO: Use a while loop controlled by attempts and authentication status.
# TODO: Print success/failure and attempts used/remaining.
