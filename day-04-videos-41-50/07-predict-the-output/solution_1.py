"""Predict the Output — While, Aliases & Conditions | Day 04.
Write predictions in README.md BEFORE executing this file.
"""

state = {"routes": ["/pay", "/status"], "enabled": True}
shadow = state.copy()
alias = state

requests = ["/pay", "/legacy", "/pay", "/status"]
index = 0
allowed_count = 0

while index < len(requests):
    route = requests[index]

    if route in shadow["routes"] and alias["enabled"]:
        allowed_count += 1
    elif route == "/legacy":
        shadow["routes"].append("/legacy")

    index += 1
else:
    print("FINISHED", index)

print(allowed_count)
print(state["routes"])
print(shadow["routes"] is state["routes"])

alias["enabled"] = False
print(shadow["enabled"])
print(state["enabled"])
print("legacy" in shadow["routes"])
print("ready" if allowed_count >= 3 else "blocked")
print((0 or "online") and not 0)
