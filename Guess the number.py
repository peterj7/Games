#Game: Guess your number
#game that guesses the user's chosen number

import random
import time

#game setup
#introduction, name, game rules
print("Game rules: [Z = go higher | X = go lower | C = correct answer]")
print("Hello, what is your name?...")
name = input()
print("Hi "+name + ", enter the highest number you want me to guess to...")
max = int(input())
print("Now pick a number between 1 and "+str(max)+" and let's begin!")
print("----------------------------------------------------------")
time.sleep(2) #gives the user 2 seconds to choose a number

#loop for the number of times it takes to get to the user's answer
#guess algorithm similar to binary search
guess = random.randint(1, max) #guessing starts at a random number
max = max + 1
min = 1
incorrect = True
tmp = -1 #holds value of past guess
while incorrect == True:
    if tmp == guess:
        break #breaks if guess was the same as last instance of guess
    tmp = guess
    print("Is your number..."+str(guess)+"?")
    userHint = input()
    if userHint.lower() == "z":
        min = guess
        guess = int(((max - min)/2)+min) #guesses between the upper half
    elif userHint.lower() == "x":
        max = guess
        guess = int(((max - min)/2)+min) #guesses between the lower half
    elif userHint.lower() == "c":
        incorrect == False
        break #correct answer
    else:
        print("Incorrect input value! Let's try that again...")
        tmp = guess - 1

print("The number you chose was "+str(guess)+". Thanks for playing "+name+"!")

