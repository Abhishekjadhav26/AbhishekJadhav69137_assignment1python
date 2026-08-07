# Abhishek_jadhav_69137
# Assignment_4  

import random
print("RANDOM PASSWORD GENERATOR")

def generate_password(length):

    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    password = ""

    for i in range(length):

        character = random.choice(characters)
        password = password + character

    return password

while True:

    print("\n1. Generate Password")
    print("2. Exit")

    choice = input("Enter Choice:")

    if choice == "1":

        length = int(input("Enter Password Length:"))
        password = generate_password(length)
        print("Generated Password =", password)

    elif choice == "2":

        print("Password Generator Closed")
        break

    else:

        print("Invalid Choice")