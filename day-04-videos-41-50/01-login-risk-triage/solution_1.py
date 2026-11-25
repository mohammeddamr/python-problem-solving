"""Login Risk Triage Queue | Day 04 | Videos 41–50.
Independent solution: see README.md. No finished solution included.
"""
# TODO: Walk through the events with a while loop.
# TODO: Apply the ordered rules with if / elif / else.
# TODO: Track approval/denial counts and unique denied users.
# TODO: Print the decisions and final summary using computed values.


# ## Requirements

# 1. Read `events` using a `while` loop and an index, **without** using a `for` loop.
# 2. For each event, determine one decision according to this **strict first-match priority**:
#    - `unknown_user`: username is not a key in `accounts`.
#    - `locked`: account exists but its `locked` field is `True`.
#    - `untrusted_ip`: event IP is not in `trusted_ips`.
#    - `invalid_password`: password check failed.
#    - `mfa_missing`: the account requires MFA but MFA check failed.
#    - Otherwise: `APPROVED`.
# 3. Every event must produce a line in this format: `01 | mona | APPROVED` or `03 | guest | DENIED: unknown_user`. Use a two-digit event number.
# 4. Count approved and denied events separately.
# 5. Store distinct denied usernames in a `set` and print them as an alphabetically sorted `list`.
# 6. Do not mutate any of the given input data structures.
# 7. Test changing account rules and adding events without changing the processing logic.

# ## Expected Output

# ```text
# 01 | mona | APPROVED
# 02 | omar | APPROVED
# 03 | guest | DENIED: unknown_user
# 04 | ali | DENIED: untrusted_ip
# 05 | sara | DENIED: invalid_password
# 06 | omar | APPROVED
# 07 | root | DENIED: locked
# 08 | mona | DENIED: mfa_missing

# Approved: 3
# Denied: 5
# Unique Denied Users: ['ali', 'guest', 'mona', 'root', 'sara']
# ```

accounts = {
    "mona": {"locked": False, "mfa_required": True},
    "omar": {"locked": False, "mfa_required": False},
    "ali": {"locked": False, "mfa_required": True},
    "sara": {"locked": False, "mfa_required": True},
    "root": {"locked": True, "mfa_required": True}
}
trusted_ips = {"10.0.0.10", "10.0.0.20"}
events = [
    {"user": "mona", "ip": "10.0.0.10", "password_ok": True, "mfa_ok": True},
    {"user": "omar", "ip": "10.0.0.20", "password_ok": True, "mfa_ok": False},
    {"user": "guest", "ip": "10.0.0.30", "password_ok": True, "mfa_ok": True},
    {"user": "ali", "ip": "10.0.0.99", "password_ok": True, "mfa_ok": True},
    {"user": "sara", "ip": "10.0.0.10", "password_ok": False, "mfa_ok": True},
    {"user": "omar", "ip": "10.0.0.20", "password_ok": True, "mfa_ok": True},
    {"user": "root", "ip": "10.0.0.10", "password_ok": True, "mfa_ok": True},
    {"user": "mona", "ip": "10.0.0.10", "password_ok": True, "mfa_ok": False}
]

i,approvedc,deniedc=0,0,0
deined=set()
while(i<len(events)):
    current_event=events[i]
    if current_event["user"]in accounts:
        current_acc=accounts[current_event["user"]]
        if not current_acc["locked"]:
            if current_event["ip"] in trusted_ips:
                if current_event["password_ok"]:
                    if current_acc["mfa_required"]:
                        if current_event["mfa_ok"]:
                            result="APPROVED"
                        else :
                            result="DENIED: mfa_missing"
                    else:
                        result="APPROVED"
                else:
                    result="DENIED: invalid_password"
            else:
                result="DENIED: untrusted_ip"
        else:
            result="DENIED: locked"
    else:
        result="DENIED: unknown_user"
    print(f"""{(i+1):02} | {current_event["user"] } | {result} """)
    if "DENIED" in result:
        deniedc+=1 
        deined.add(current_event["user"])
    else : 
        approvedc+=1
    
    
    i+=1
print(f""" 
Approved: {approvedc}
Denied: {deniedc}
Unique Denied Users: {sorted(list(deined))}
""")