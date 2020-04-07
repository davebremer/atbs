import sys
import random

theNum = random.randint(1, 10)

print("I am thinking of a number between 1 and 20.")
match = False

numGuesses = 0

while not match:
    guessing = ""    
    while  not guessing.isnumeric() or not 0 < int(guessing) < 21: 
        guessing = input("Take a guess between 1 and 20: ")

    theGuess = int(guessing)
    numGuesses += 1

    if theNum == theGuess:
        match = True
        print("Good job! You guessed my number in " + str(numGuesses) + " guesses!")

    elif theGuess < theNum:
        print("Your guess is too low")
    else:
        print("Your guess is too high")