import itertools
import string

def bruteforce_attack(password):
    chars = string.printable.strip()
    attempts = 0
    for length in range(1,len(password) +1):
        for guess in itertools.product(chars,repeat=length):
            attempts += 1
            guess = "".join(guess)
            if guess == password:
                return (attempts,guess)
    return (attempts,None)

password = input("Input the password to crack:")
attempts,guess = bruteforce_attack(password)
if guess:
    print(f"Password cracked in {attempts} attempts. The password is{guess}.")
else:
    print(f"password not cracked after{attempts} attempts.")

#In the above we ultilize the string module to get all possible characters that could be used in a password.The itertools.product function generates all possible combinations of characters up to the password length.The programme then checks each combination to see if it matches the password.The number of attempts to crack the password is recorded and printed out at the end of the programme.


