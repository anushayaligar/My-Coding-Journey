import string
import random

letters = string.ascii_letters
digits = string.digits
symbols  = string.punctuation

all_chars=letters+digits+symbols
 
length = int(input("enter the length of password: "))

password = ""
for i in range(length):
    char = random.choice(all_chars)
    password += char

print(f"you random password is: {password}")
