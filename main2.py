#!/usr/bin/env python3
import sys
import random
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"
number = random.randrange(1,20)
guesses = 1
while guesses <= 3:
    guess = input("Guess a number from 1 to 20: ")
    while guess.isnumeric() == False:
        guess = input("Please enter an integer between 1 and 20: ")
    if int(guess) == number:
        print("Great job! You got it!")
        break
    elif (guesses < 3 and guess != number):
        print("Sorry, that's not correct. Try again?")
        guesses = guesses + 1
    elif (guesses == 3 and guess != number):
        print("Sorry, you're out of guesses! The number was: " + str(number))
        break
