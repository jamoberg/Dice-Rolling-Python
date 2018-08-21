#!/usr/bin/python
import random

min = 1
max = 6
rollAgain = "yes"

while rollAgain == "y" or rollAgain == "yes" :
    print("\nDice rolled: " + str(random.randint(min, max)) + "!\n")
    rollAgain = raw_input("Wanna roll again? ")
