"""Email Alias Verification Parser

Day 03 | Videos 31–40
First independent solution. No completed solution included.
See README.md for requirements and example output.
"""
# TODO: Normalize the email and locate dynamic separators.
# TODO: Extract base username, alias tag, and domain.
# TODO: Build the masked address without a fixed number of stars.
# TODO: Compute and print the Boolean checks.

# Requirements
# 1. Read a tagged address from the user, strip surrounding whitespace, and lowercase it.
# 2. Find the position of `+` and `@` dynamically with `find()` (no hardcoded character offsets).
# 3. Extract three parts: `base_username`, `alias_tag`, and `domain`.
# 4. Generate `masked_email`: keep the first two and last two characters of the base username, mask its middle with `*`, then retain the `+tag@domain` suffix.
# 5. Compute `single_at`: the normalized input contains exactly one `@`.
# 6. Compute `trusted_domain`: domain equals `example.com` OR `company.org`.
# 7. Compute `valid_alias`: base username has at least 6 characters AND alias tag at least 2 characters AND `single_at` AND `trusted_domain`.
# 8. Display the normalized email, all parsed fields, masked email, and Boolean flags.
# 
# Expected Output
# ```text
# Normalized: nora.dev+ops@example.com
# Base Username: nora.dev
# Alias: ops
# Domain: example.com
# Masked: no****ev+ops@example.com
# Single @: True
# Trusted Domain: True
# Valid Alias: True
# ```

raw_email = input("Tagged email: ")
email=raw_email.strip().lower()
pplus=email.find("+")
pat=email.find("@")

username=email[0:pplus]
alias=email[pplus+1:pat]
domain=email[pat+1:]
masked=username[0:2] + "*"*(len(username)-4) +username[-2:]+"+"+alias+"@"+domain
single_at=email.count("@") ==1
trusted_domain= domain == "example.com" or "example.com"
valid_alias= len(username)>=6 and len(alias)>=2 and single_at and trusted_domain

print(f"""
# ```text
# Normalized: {email}
# Base Username: {username}
# Alias: {alias}
# Domain: {domain}
# Masked: {masked}
# Single @: {single_at}
# Trusted Domain: {trusted_domain}
# Valid Alias: {valid_alias}
# ```
""")