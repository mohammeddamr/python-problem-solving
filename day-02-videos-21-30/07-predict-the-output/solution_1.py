"""Predict the Output — Mutability Trap

Day 02 | Videos 21–30
Before running, write all your output predictions in README.md.
"""

a = [3, 1, 3, 2]
b = a.copy()

removed = a.remove(3)

a.sort()
b.reverse()

pair = ("api",) * 2 + ("db",)

permissions = {"read", "write"}
returned = permissions.update({"deploy"})

data = {
    "level": 1,
    "level": 2,
    "scores": b
}

print(a)
print(b)
print(removed)
print(pair.count("api"))
print(pair[-1])
print(returned)
print(permissions.issuperset({"read", "deploy"}))
print(data["level"], data["scores"][0])
