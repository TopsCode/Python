import re

# Email pattern
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email = "test@example.com"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
