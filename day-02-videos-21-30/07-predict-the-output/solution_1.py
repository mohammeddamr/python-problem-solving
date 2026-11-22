"""Predict the Output — Mutability Trap

Day 02 | Videos 21–30
Before running, write all your output predictions in README.md.
"""

a = [3, 1, 3, 2]
b = a.copy()

removed = a.remove(3) #a=132 removed=none

a.sort()#a=123
b.reverse()#b=2313

pair = ("api",) * 2 + ("db",) #pair=api api db

permissions = {"read", "write"}
returned = permissions.update({"deploy"}) #retuerned=none   permissions=read write deploy

data = {
    "level": 1,
    "level": 2,
    "scores": b#b=2313
}

print(a)#a=123
print(b)#b=2313
print(removed)#none
print(pair.count("api")) #2
print(pair[-1])#db
print(returned)#none
print(permissions.issuperset({"read", "deploy"}))#true
print(data["level"], data["scores"][0])#2 2