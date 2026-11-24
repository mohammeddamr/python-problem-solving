"""Predict the Output — Dictionary & Boolean Traps

Day 03 | Videos 31–40
First independent solution. No completed solution included.
See README.md for requirements and example output.
"""

settings = {"attempts": "3", "active": True}
alias = settings #that is still linked any change for any ith them will happen for both because both have the same refrence
snapshot = settings.copy() #that is shallow copy but will be linked if there is a deeper levels 

new_region = settings.setdefault("region", "eu") #setting={"attempts": "3", "active": True,"region":"eu"}
old_attempts = settings.setdefault("attempts", 99) #setting={"attempts": "3", "active": True,"region":"eu"}

settings["attempts"] = int(settings["attempts"]) #settings = {"attempts": 3, "active": True ,"region":"eu"}
settings["attempts"] += 2 #settings = {"attempts": 5, "active": True , "region":"eu"}

update_result = settings.update({"enabled": False}) #settings = {"attempts": 5, "active": True,"region":"eu", "enabled": False}
last_pair = settings.popitem() #settings = {"attempts": 5, "active": True,"region":"eu"} laxt_pair= ("enabled", False)

check = (settings["attempts"] >= 5 and settings["active"]) or (
    not settings.get("enabled", False)
)

print(new_region) #eu
print(old_attempts)#"3"
print(snapshot["attempts"])#"3"
print(alias["attempts"])#5
print(update_result) #None
print(last_pair)#("enabled", False)
print(check) #True
print((0 or "ready") and not "")# True
print(settings.get("missing", "none"))#none

# ## My Predictions (complete before execution)

# | Print # | Predicted output | Reasoning |
# |---|---|---|
# | 1 | _Fill in_ | _Explain_ |
# | 2 | _Fill in_ | _Explain_ |
# | 3 | _Fill in_ | _Explain_ |
# | 4 | _Fill in_ | _Explain_ |
# | 5 | _Fill in_ | _Explain_ |
# | 6 | _Fill in_ | _Explain_ |
# | 7 | _Fill in_ | _Explain_ |
# | 8 | _Fill in_ | _Explain_ |
# | 9 | _Fill in_ | _Explain_ |
