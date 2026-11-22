"""API Deployment Readiness Report

Day 02 | Videos 21–30
First independent solution. No finished solution included.
"""

# ## Requirements

# 1. Normalize the service name to `payments-api`.
# 2. Format the version tuple as `2.5.0`.
# 3. Count original routes and occurrences of `/pay`.
# 4. Determine how many unique routes exist.
# 5. Find required routes missing from the current routes.
# 6. Find deprecated routes that are currently present.
# 7. Build a corrected route set by removing deprecated routes and adding missing required routes.
# 8. Verify the corrected routes include everything required and nothing deprecated.
# 9. Display the final routes sorted alphabetically in a list.
# 10. Convert uptime seconds to days, hours, minutes and seconds; print clock values using two-digit formatting.

# ## Expected output

# ```text
# ======= DEPLOYMENT REPORT =======
# Service: payments-api
# Version: 2.5.0

# Original Route Count: 5
# Unique Route Count: 4
# /pay Occurrences: 2

# Missing: {'/health'}
# Deprecated: {'/legacy'}

# Final Routes:
# ['/health', '/pay', '/refund', '/status']

# All Required Present: True
# No Deprecated Routes: True

# Server Uptime: 1 days, 01:47:45
# =================================
# ```

config = {
    "service": {
        "name": "  PAYMENTS--API  ",
        "version": (2, 5, 0)
    },
    "routes": [
        "/pay",
        "/refund",
        "/pay",
        "/status",
        "/legacy"
    ],
    "required": {
        "/pay", "/refund", "/status", "/health"
    },
    "deprecated": {"/legacy"},
    "uptime_seconds": 92865
}
# TODO: Implement your calculations and print the requested output.

config["service"]["name"]=config["service"]["name"].lower().strip().replace("--","-")
config["service"]["version"]=f"{config["service"]["version"][0]}.{config["service"]["version"][1]}.{config["service"]["version"][2]}"
orgrc=len(config["routes"])

rset=set(config["routes"])
rrset=set(config["required"])
rdset=set(config["deprecated"])

unirc=len(rset)
payoc=config["routes"].count("/pay")
missing=rrset.difference(rset)
deprecated=rset.intersection(rdset)

final=list(rrset)
final.sort()

day=92865//(60*60*24)
h=(92865%(60*60*24))//(60*60)
min=((92865%(60*60*24))%(60*60))//60
sec=((92865%(60*60*24))%(60*60))%60

print(f"""
# ```text
# ======= DEPLOYMENT REPORT =======
# Service: {config["service"]["name"]}
# Version: {config["service"]["version"]}

# Original Route Count: {orgrc}
# Unique Route Count: {unirc}
# /pay Occurrences: {payoc}

# Missing: {missing}
# Deprecated: {deprecated}

# Final Routes:
# {final}

# All Required Present: {rrset.issubset(rrset)}
# No Deprecated Routes: {rrset.isdisjoint(rdset)}

# Server Uptime: {day} days, {h:02}:{min:02}:{sec:02}
# =================================
# ```      
""")