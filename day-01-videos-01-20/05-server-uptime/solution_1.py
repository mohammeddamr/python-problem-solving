"""Server Uptime Calculator

Day 01 | Videos 1–20
First independent solution. No finished solution included.
"""

# ## Requirements

# 1. Convert the total seconds into complete days.
# 2. Calculate the remaining hours, minutes, and seconds.
# 3. Display each component and a combined uptime string.

# ## Expected output

# ```text
# SERVER UPTIME
# -------------
# Days: 11
# Hours: 10
# Minutes: 20
# Seconds: 54

# Uptime: 11 days, 10:20:54
# ```

total_seconds = 987654

# TODO: Implement your calculations and print the requested output.
days=(total_seconds//(60*60*24))
daysR=total_seconds%(60*60*24)
hours=daysR//(60*60)
hoursR=daysR%(60*60)
minutes=hoursR//60
seconds=hoursR%60

print(f"""SERVER UPTIME
# -------------
# Days: {days}
# Hours: {hours:02d}
# Minutes: {minutes:02d}
# Seconds: {seconds:02d}

# Uptime: {days} days, {hours:02d}:{minutes:02d}:{seconds:02d}""")