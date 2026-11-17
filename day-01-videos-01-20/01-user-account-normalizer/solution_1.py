"""User Account Normalizer

Day 01 | Videos 1–20
First independent solution. No finished solution included.
"""

raw_name = " \t###mOHaMeD    aMr### \n"
raw_role = "   BACKEND   eNGINEER   "
user_id = "74"

# TODO: Implement your calculations and print the requested output.
name=" ".join(raw_name.strip().strip("#").title().split())
userName=name.lower().replace(" ",".")
role=" ".join(raw_role.strip().capitalize().split())
userId= "DEV-"+user_id.zfill(6) #True

print(f"Fullname:{name}\nUsername:{userName}\nRole:{role}\nId:{userId}")