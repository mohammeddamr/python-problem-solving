"""Immutable Server Metrics

Day 02 | Videos 21–30
First independent solution. No finished solution included.
"""

# ## Requirements

# 1. Use tuple unpacking to assign the server ID, service name, readings tuple, and date to separate variables.
# 2. Normalize the service name as `Api Gateway`.
# 3. Count occurrences of `135` in the original readings tuple.
# 4. Find the index of its first appearance.
# 5. Create a new tuple with a reading `150` appended; do not change the original tuple.
# 6. Slice out the last three readings from the new tuple.
# 7. Calculate the mean of those three numbers without loops or `sum()`.
# 8. Print the mean to exactly two decimal places.

# ## Expected output

# ```text
# SERVER: SRV-19
# SERVICE: Api Gateway
# DATE: 2026-11-18

# 135 Occurrences: 3
# First 135 Index: 1

# Original: (120, 135, 135, 140, 135, 125)
# Updated: (120, 135, 135, 140, 135, 125, 150)

# Last 3: (135, 125, 150)
# Last 3 Average: 136.67
# ```

session = (
    "SRV-19",
    "  api_gateway  ",
    (120, 135, 135, 140, 135, 125),
    "2026-11-18"
)
# TODO: Implement your calculations and print the requested output.
server,service,values,date=session

c135=values.count(135)
i135=values.index(135)
nv=values + (150,)
nv[-3:]
avg=(nv[-1]+nv[-2]+nv[-3])/3

print(f"""# ```text
# SERVER: {server}
# SERVICE: {service.strip().title().replace("_"," ")}
# DATE: {date}

# 135 Occurrences: {c135}
# First 135 Index: {i135}

# Original: {values}
# Updated: {nv}

# Last 3: {nv[-3:]}
# Last 3 Average: {avg:.2f}
# ```""")