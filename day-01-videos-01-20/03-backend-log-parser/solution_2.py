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
log = "  [ERROR] :: service=PAYMENTS :: code=503 :: message=GATEWAY_TIMEOUT  ".lower()

# TODO: Implement your calculations and print the requested output.

severity_end=log.find("::")
service_start=log.find("service")
service_end=log.find("::",service_start)
code_start=log.find("code")
code_end=log.find("::",code_start)
msg_start=log.find("message")

severity=log[0:severity_end]
service=log[service_start:service_end]
code=log[code_start:code_end]
message=log[msg_start:]
print(message,severity,code,service)