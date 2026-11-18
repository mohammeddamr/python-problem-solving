"""Gaming Leaderboard Engine

Day 02 | Videos 21–30
First independent solution. No finished solution included.
"""

# ## Requirements

# 1. Keep `scores` unchanged.
# 2. Make a separate list of all scores sorted in descending order (including duplicates).
# 3. Create a new list of unique scores, sorted in descending order.
# 4. Get the top three distinct scores.
# 5. Count how many players scored exactly `95`.
# 6. Find the first index of `91` in the **original** score list.
# 7. Print a three-line leaderboard using the values from the distinct-score list.

# ## Expected output

# ```text
# Sorted Scores:
# [99, 95, 95, 91, 91, 88, 88, 82, 74, 74]

# Unique Top 3: [99, 95, 91]
# Players with 95: 2
# First 91 Index: 3

# LEADERBOARD
# 1st: 99
# 2nd: 95
# 3rd: 91
# ```

scores = [88, 95, 88, 91, 74, 95, 82, 91, 99, 74]
# TODO: Implement your calculations and print the requested output.
s1=scores.copy()
s1.sort(reverse=True)
s=scores.copy()
u=set(s)
s=list(u)
s.sort(reverse=True)
scores.count(95)
scores.index(91)

print(f"""
# ```text
# Sorted Scores:
# {s1}

# Unique Top 3: {s[0:3]}
# Players with 95: {scores.count(95)}
# First 91 Index: {scores.index(91)}

# LEADERBOARD
# 1st: {s[0]}
# 2nd: {s[1]}
# 3rd: {s[2]}
# ```""")