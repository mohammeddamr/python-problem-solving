"""Backend Log Parser

Day 01 | Videos 1–20
First independent solution. No finished solution included.
"""
# ## Requirements

# 1. Extract the severity, service, code, and message from the log.
# 2. Locate field boundaries with `find()` and string slicing rather than fixed offsets.
# 3. Format the message in title case, replacing the underscore with a space.
# 4. Display the parsed fields.

# ## Expected output

# ```text
# Severity: ERROR
# Service: payments
# Code: 503
# Message: Gateway Timeout
# ```
log = "  [ERROR] :: service=PAYMENTS :: code=503 :: message=GATEWAY_TIMEOUT  "

# TODO: Implement your calculations and print the requested output.
logs=log.strip().split("::")

severity=logs[0].strip().upper()
service=(logs[1].strip().split("="))[1]
code=(logs[2].strip().split("="))[1]
message=(logs[3].strip().split("="))[1].title()
print(message,severity,code,service)