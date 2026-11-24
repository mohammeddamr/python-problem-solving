"""Authentication Policy Matrix

Day 03 | Videos 31–40
First independent solution. No completed solution included.
See README.md for requirements and example output.
"""
# TODO: Extract and convert the necessary values for both accounts.
# TODO: Express the three policy flags for each account.
# TODO: Compute allowed login count without loops; print your results.

# Requirements
# 1. Convert each account’s `credits` string to an integer; retain the original account data unchanged.
# 2. For EACH account compute `login_allowed`: verified AND not locked AND failed attempts below maximum AND (MFA enabled OR policy permits verified accounts without MFA).
# 3. For EACH account compute `billing_allowed`: login allowed AND numeric credits greater than or equal to required billing credits.
# 4. For EACH account compute `needs_review`: locked OR attempts at/above the maximum OR not verified.
# 5. Count how many accounts have `login_allowed == True` without loops (there are exactly two named accounts).
# 6. Print the three flags per account and total permitted logins.
# 7. Use meaningful parentheses: the policy must not silently change due to Boolean precedence.
# 
# Expected Output
# 
# ```text
# PRIMARY (dev01)
# Login Allowed: True
# Billing Allowed: False
# Needs Review: False
# 
# BACKUP (ops02)
# Login Allowed: False
# Billing Allowed: False
# Needs Review: True
# 
# Allowed Login Count: 1
# ```


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

pcredits=int(accounts["primary"]["credits"])
bcredits=int(accounts["backup"]["credits"])

plogin_allowed=accounts["primary"]["verified"] and (not accounts["primary"]["locked"]) and ( accounts["primary"]["failed_attempts"] < policy.get("max_failed_attempts")) and (accounts["primary"]["mfa"] | policy["allow_verified_without_mfa"])
blogin_allowed=accounts["backup"]["verified"] and (not accounts["backup"]["locked"]) and ( accounts["backup"]["failed_attempts"] < policy.get("max_failed_attempts")) and (accounts["backup"]["mfa"] | policy["allow_verified_without_mfa"])

pbilling_allowed=plogin_allowed and (pcredits>=policy["min_billing_credits"])
bbilling_allowed=blogin_allowed and (bcredits>=policy["min_billing_credits"])

pneeds_review=accounts["primary"]["locked"] or (not accounts["primary"]["verified"]) or (accounts["primary"]["failed_attempts"] >= policy.get("max_failed_attempts"))
bneeds_review=accounts["backup"]["locked"] or (not accounts["backup"]["verified"]) or (accounts["backup"]["failed_attempts"] >= policy.get("max_failed_attempts"))

allowed_login_count= plogin_allowed + blogin_allowed

print(f""" 
# ```text
# PRIMARY {accounts["primary"]["username"]}
# Login Allowed: {plogin_allowed}
# Billing Allowed: {pbilling_allowed}
# Needs Review: {pneeds_review}
# 
# BACKUP {accounts["backup"]["username"]}
# Login Allowed: {blogin_allowed}
# Billing Allowed: {bbilling_allowed}
# Needs Review: {bneeds_review}
# 
# Allowed Login Count: {allowed_login_count}
# ```
""")