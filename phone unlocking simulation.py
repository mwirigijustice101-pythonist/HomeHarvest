
import random

password = "justice123"
otp = str(random.randint(1000, 9999))  # generate 4-digit OTP

print("Your OTP is:", otp)  # In real life, this would be sent via SMS/email

attempt = input("Enter password: ")
if attempt == password:
    otp_attempt = input("Enter OTP: ")
    if otp_attempt == otp:
        print("Phone unlocked (simulation) ✅")
    else:
        print("Invalid OTP ❌")
else:
    print("Invalid password ❌")
