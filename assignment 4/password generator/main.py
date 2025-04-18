
#password generator

import random
import string  

def generatepassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))

    return password
length= int(input("Enter the password length:"))

if __name__ == "__main__":
    print("Generated Password:" , generatepassword(length))



