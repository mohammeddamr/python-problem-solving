"""Predict the Output — Dictionary & Boolean Traps

Day 03 | Videos 31–40
First independent solution. No completed solution included.
See README.md for requirements and example output.
"""

settings = {"attempts": "3", "active": True}
alias = settings
snapshot = settings.copy()

new_region = settings.setdefault("region", "eu")
old_attempts = settings.setdefault("attempts", 99)

settings["attempts"] = int(settings["attempts"])
settings["attempts"] += 2

update_result = settings.update({"enabled": False})
last_pair = settings.popitem()

check = (settings["attempts"] >= 5 and settings["active"]) or (
    not settings.get("enabled", False)
)

print(new_region)
print(old_attempts)
print(snapshot["attempts"])
print(alias["attempts"])
print(update_result)
print(last_pair)
print(check)
print((0 or "ready") and not "")
print(settings.get("missing", "none"))
