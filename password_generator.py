import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#µ^-_"

number = int(input("How many letters do you need ? "))

for _ in range(number):
    random_letter = random.choice(chars)
    print(random_letter, end='')
