"""API Deployment Console

Day 03 | Videos 31–40
First independent solution. No completed solution included.
See README.md for requirements and example output.
"""

# TODO: Normalize service, unpack version, and normalize operator.
# TODO: Audit and reconcile routes using List and Set operations.
# TODO: Convert and calculate capacity and uptime.
# TODO: Compute approval/readiness Boolean expressions and print report.

# ## Example User Input
# Enter these values at the prompts, one per line:

# ```text
#   mONA  aLI  
# 125
# 93784
# yes
# ```

# ## Requirements

# 1. Normalize service name to `payments-gateway`.
# 2. Unpack the version tuple and print `major.minor.patch` without printing parentheses or commas.
# 3. Read and normalize the operator’s name, convert extra slots and uptime seconds to integers, and parse approval as a Boolean.
# 4. Compute original route count, unique route count, and `/pay` occurrence count.
# 5. Determine required routes missing from the current routes, and deployed routes that are deprecated.
# 6. Make a new set of final routes with deprecated routes removed and missing required routes added (do not alter the input `routes` list).
# 7. Print the final routes sorted alphabetically as a List.
# 8. Convert the capacity and in-use strings to integers; reserve the requested extra slots and compute remaining capacity.
# 9. Calculate uptime as days, hours, minutes, seconds with padded `HH:MM:SS`.
# 10. Compute `routes_ready`: all required routes included in final routes AND final routes disjoint from deprecated routes.
# 11. Compute `capacity_ok`: projected usage does not exceed capacity and extra slots are positive.
# 12. Compute `runtime_ok`: uptime is at least 86,400 seconds.
# 13. Compute `deploy_ready`: operator approved AND routes ready AND capacity OK AND runtime OK.

# ## Expected Output

# ```text
# Service: payments-gateway
# Version: 3.2.1
# Operator: Mona Ali
# Original Route Count: 4
# Unique Route Count: 3
# /pay Occurrences: 2
# Missing: {'/health'}
# Deprecated: {'/legacy'}
# Final Routes: ['/health', '/pay', '/refund']
# Uptime: 1 days, 02:03:04
# Capacity: 1500
# Projected Usage: 1110
# Remaining Capacity: 390
# Approved: True
# Routes Ready: True
# Capacity OK: True
# Runtime OK: True
# Deploy Ready: True
# ```


deployment = {
    "service": {"name": "  PAYMENTS--GATEWAY  ", "version": (3, 2, 1)},
    "routes": ["/pay", "/refund", "/pay", "/legacy"],
    "required": {"/pay", "/refund", "/health"},
    "deprecated": {"/legacy"},
    "limits": {"capacity": "1500", "in_use": "985"}
}

operator_raw = input("Operator name: ")
extra_slots_raw = input("Extra slots to reserve: ")
uptime_raw = input("Uptime in seconds: ")
approval_raw = input("Release approved (yes/no): ")

normalized_service=deployment["service"]["name"].strip().lower().replace("--","-")
major,minor,patch=deployment["service"]["version"]
name=" ".join(operator_raw.strip().lower().title().split())
extra_slots=int(extra_slots_raw)
uptime=int(uptime_raw)
approval=approval_raw.lower()== "yes" 
org_route_count=len(deployment["routes"])
unique_route_count=len(set(deployment["routes"]))
pay_occ_count=deployment["routes"].count("/pay")
req=set(deployment["required"])
org=set(deployment["routes"])
dep=set(deployment["deprecated"])
missing=req-org #missing=req.difference(org)
deprecated=org&dep #deprecated=req.intersection(dep)
final=(org-dep).union(req)
capcity=int(deployment["limits"]["capacity"])
in_use=int(deployment["limits"]["in_use"])
uptime=int(uptime_raw)
days=uptime//(60*60*24)
days_rem=uptime%(60*60*24)
hours=days_rem//(60*60)
hours_rem=days_rem%(60*60)
mins=hours_rem//60
secs=hours_rem%60

routes_ready=final.issuperset(req) and final.isdisjoint(dep)
capacity_ok=capcity >= (in_use+extra_slots) and extra_slots>0
runtime_ok=uptime>=86400
deploy_ready=approval and routes_ready and capacity_ok and runtime_ok

print(f"""
# ```text
# Service: {normalized_service}
# Version: {major}.{minor}.{patch}
# Operator: {name}
# Original Route Count: {org_route_count}
# Unique Route Count: {unique_route_count}
# /pay Occurrences: {pay_occ_count}
# Missing: {missing}
# Deprecated: {deprecated}
# Final Routes: {sorted(final)}
# Uptime: {days:02d} days, {hours:02d}:{mins:02d}:{secs:02d}
# Capacity: {capcity}
# Projected Usage: {in_use + extra_slots}
# Remaining Capacity: {capcity - (in_use + extra_slots)}
# Approved: {approval}
# Routes Ready: {routes_ready}
# Capacity OK: {capacity_ok}
# Runtime OK: {runtime_ok}
# Deploy Ready: {deploy_ready}
# ```
""")