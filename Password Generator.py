import random
import string
length=int(input("Enter the length of the password: "))
Random=random.choice(string.ascii_lowercase)
Random1=random.choice(string.ascii_uppercase)
password=""
for i in range (length):
    password+=random.choice(string.ascii_lowercase)+random.choice(string.ascii_uppercase)
print(password)