"""
f you don't have the security device in your possession,
here is a useful procedure:
- multiply the number by 47,
- keep the last 5 digits,
- reverse them,
- multiply by 59,
- enter the last 5 digits
before the temporary code changes. That's it!
"""

token = 48216
print(token)

# multiply the number by 47,
token *= 47
print(f"47 : {token}")

# keep the last 5 digits,
token = str(token)[-5:]
print(f"5 digit : {token}")

# reverse them,
token = int(token[::-1])
print(f"reverse : {token}")

# multiply by 59,
token *= 59
print(f"*59 {token}")

# enter the last 5 digits
token = str(token)[-5:]
print(f"5 digit : {token}")