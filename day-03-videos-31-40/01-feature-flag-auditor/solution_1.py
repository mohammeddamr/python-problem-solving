"""Feature Flag Rollout Auditor

Day 03 | Videos 31–40
First independent solution. No completed solution included.
See README.md for requirements and example output.
"""
# ## Requirements

# 1. Create a shallow copy of `settings` named `working` so top-level changes do not modify the original.
# 2. Normalize the app name in `working` to `rajeaa-api` (remove outer spaces, lowercase, replace `--` with `-`).
# 3. Apply all entries from `changes` to `working` using a Dictionary Method.
# 4. Add a `region` key with default value `me-central` only if it is absent.
# 5. Read `timeout_seconds` with fallback `30` **without inserting that key**.
# 6. Remove the old `version` field from `working` and store the removed value.
# 7. Remove and capture the most recently inserted pair from the separate `audit` dictionary.
# 8. Calculate remaining requests (`limit - used`).
# 9. Calculate `quota_healthy`: used requests are strictly less than the limit.
# 10. Calculate `beta_rollout_allowed`: production environment **AND** healthy quota **AND** audit logs enabled **AND NOT** beta already enabled.
# 11. Display original vs working environment, and verify the original still has six top-level keys.

# ## Expected Output

# ```text
# APP: rajeaa-api
# Original Environment: staging
# Working Environment: production
# Region: me-central
# Timeout Fallback: 30
# Removed Version: 2.4.1
# Last Audit Pair: ('build', '2026.11')
# Remaining Requests: 2025
# Quota Healthy: True
# Beta Rollout Allowed: True
# Original Key Count: 6
# ```

settings = {
    "app_name": "  rAjeAA--API  ",
    "environment": "staging",
    "version": "2.4.1",
    "requests_limit": 2000,
    "requests_used": 1475,
    "features": {"audit_logs": True, "beta_access": False}
}

changes = {"environment": "production", "requests_limit": 3500}

audit = {"status": "pending", "reviewer": "backend", "build": "2026.11"}

# TODO: Copy and update the working settings.
# TODO: Use dictionary methods; compute all policy flags.
# TODO: Print the report (never hardcode calculated values).

working=settings.copy()
working["app_name"]=working["app_name"].strip().lower().replace("--","-")
working.update(changes)
working.setdefault("region","me-central")
working.get("timeout_seconds","30")
removed_version=working.pop("version")
latest_audit=audit.popitem()
request_remaining=working["requests_limit"]-working["requests_used"]
quota_healthy=request_remaining<working["requests_limit"]
beta_rollout_allowed=working["environment"] and quota_healthy and working["features"]["audit_logs"] and (not working["features"]["beta_access"] )

#production environment **AND** healthy quota **AND** audit logs enabled **AND NOT** beta already enabled.

print(f""" 

# APP: {working["app_name"]}
# Original Environment: {settings["environment"]}
# Working Environment: {working["environment"]}
# Region: {working["region"]}
# Timeout Fallback: {working.get("timeout_seconds",30)}
# Removed Version: {removed_version}
# Last Audit Pair: {latest_audit}
# Remaining Requests: {request_remaining}
# Quota Healthy: {quota_healthy}
# Beta Rollout Allowed: {beta_rollout_allowed}
# Original Key Count: {len(settings)}
""")