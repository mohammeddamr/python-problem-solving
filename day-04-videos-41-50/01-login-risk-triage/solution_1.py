"""Login Risk Triage Queue | Day 04 | Videos 41–50.
Independent solution: see README.md. No finished solution included.
"""

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
# TODO: Walk through the events with a while loop.
# TODO: Apply the ordered rules with if / elif / else.
# TODO: Track approval/denial counts and unique denied users.
# TODO: Print the decisions and final summary using computed values.
