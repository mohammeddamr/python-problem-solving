"""Predict the Output — Bonus.

Before running this file, write your predicted output and explanations
in README.md. Then execute it to check your predictions.
"""

a = "##PyTHon--BACKEND##"
b = a.strip("#").replace("--", "-").lower()

print(b[2:8])
print(b[-7:-1])
print(b.count("n"))

x = 5 + 2 ** 3 * 4 // 3 % 5
print(x)
