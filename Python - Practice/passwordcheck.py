import os
import random

u_pwd = input("Enter a password: ")
pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
       '1', '2', '3', '4', '5', '6']

pw = ""

while pw != u_pwd:
    pw = ""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[random.randint(0, len(pwd) - 1)]
        pw += str(guess_pwd)
    print("Cracking Password... Please wait:", pw)

print("Your Password Is:", pw)
