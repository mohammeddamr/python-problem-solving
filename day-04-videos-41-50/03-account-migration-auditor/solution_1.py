"""Account Migration Auditor | Day 04 | Videos 41–50.
Independent solution: see README.md. No finished solution included.
"""

raw_accounts = [
    {"email": "  Mona.ALI@Example.COM ", "role": "Admin", "active": True},
    {"email": "omar@example.com", "role": "member", "active": True},
    {"email": "mona.ali@example.com", "role": "admin", "active": True},
    {"email": "guest@unsafe.net", "role": "member", "active": True},
    {"email": "noura@example.com", "role": "EDITOR", "active": False},
    {"email": " yusuf@example.com ", "role": "Editor", "active": True},
    {"email": "bad-email", "role": "admin", "active": True}
]
allowed_domains = {"example.com", "company.org"}
allowed_roles = {"admin", "editor", "member"}
# TODO: Normalize and validate records with while + if / elif / else.
# TODO: Use set membership to detect already-migrated emails.
# TODO: Print decisions, counters, and the ordered migrated list.
