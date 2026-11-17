"""Email Privacy Masking

Day 01 | Videos 1–20
First independent solution. No finished solution included.
"""
#```text
# Original: mohamed.amr@example.com
# Masked: mo*******mr@example.com
# Domain: example.com
# ````
raw_email = "  Mohamed.AMR@Example.COM \t"

# TODO: Implement your calculations and print the requested output.
email=raw_email.strip().lower()
splited_email=email.split("@")
domain=splited_email[1]
masked=splited_email[0][0] + splited_email[0][1] + "*"*(len(splited_email[0])-4) +splited_email[0][-2] + splited_email[0][-1] +"@"+splited_email[1]


print(f"{email}\n{masked}\n{domain}")