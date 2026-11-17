"""Predict the Output — Bonus.

Before running this file, write your predicted output and explanations
in README.md. Then execute it to check your predictions.
"""

# ## Requirements

# 1. Write down the value of `b`.
# 2. Predict each string output.
# 3. Trace the arithmetic expression using Python precedence rules.
# 4. Run the file to check your prediction.

# ## Expected output

# ```text
# Predict all four printed lines before running the file.
# Explain your reasoning for slicing and arithmetic precedence.
# ```

a = "##PyTHon--BACKEND##"
b = a.strip("#").replace("--", "-").lower() # python-backend

print(b[2:8]) #thon-b
print(b[-7:-1]) #backen
print(b.count("n")) #2

x = 5 + 2 ** 3 * 4 // 3 % 5 
print(x) #5
