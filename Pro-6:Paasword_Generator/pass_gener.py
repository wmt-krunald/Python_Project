import random

character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+-*/<>?/.[,]0123456789"

num = int(input("\nEnter the number of Passwords you Want : "))
length = int(input("\nWhat is the length of your password : "))

for p in range(num):
    passwords = ""
    for c in range(length):
        passwords += random.choice(character)
    print("\n",passwords)