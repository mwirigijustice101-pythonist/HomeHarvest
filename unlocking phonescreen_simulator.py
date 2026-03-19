
# Simple lock screen simulator in Python
password = "justice123"

attempt = input("Enter password to unlock: ")

if attempt == password:
    print("Phone unlocked (simulation) ✅")
else:
    print("Invalid password ❌")

