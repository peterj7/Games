#Game: Monty Hall Problem
#game from Monty Hall's "Let's make a deal"
#

import random
import time
import os

#list of possible doors in the game
doors = ['''

 +-----+
 |     |
 |     |
 |0    |
 |     |
 |     |
=========''', '''



 
 ^..^
( oo )  )~
  ,,  ,,
=========''', '''



   __
 _| =\__
/o____o_\

=========''']

#game setup
#introduction, name, game rules
print("Monty Hall Problem")
print("Game rules: [Choose door by entering 1, 2, or 3. | Yes = 1, No = 0]")
print("            Enter an empty answer anytime to quit the game")
print("Hello, what is your name?...")
name = input()
print("Hi "+name+", lets begin!")
print("-----------")

keepPlaying = True
gamesPlayed = 0
switchDoors = 0
switchWin = 0
unswitchWin = 0
goatDoors = []
while keepPlaying == True: #continues through each instance of the game as long as it is True and keeps player stats
    gamesPlayed = gamesPlayed + 1
    carDoor = random.randint(0, 2) #random int to determine which door is the answer
    openDoor = random.randint(0, 1)
    for i in range(0,3): #prints initial set of doors
        print(doors[0])
    print("Choose a door")
    originalDoor = int(input())-1
    for i in range(0,3): #makes a list length 2 of doors that have goats behind it
            if i != originalDoor:
                goatDoors.append(i)
    if originalDoor == carDoor: #random door shown if original door chosen is actual answer
        for i in range(0,3):
            if goatDoors[openDoor] == i:
                print(doors[1])
            else:
                print(doors[0])
    else: #shows the only possible goat door because chose door is also goat
        for i in range(0,3):
            if i != originalDoor and i != carDoor:
                for j in range(0,3):
                    if j == i:
                        print(doors[1])
                    else:
                        print(doors[0])
                break

    print("Would you like to switch doors?")
    while True: #loops until valid answer input
        switch = int(input())
        if switch != 1 and switch != 0:
            print("Would you like to switch doors?")
        else:
            break
    if switch == 1:
        switchDoors = switchDoors + 1
    for i in range(0,3): #reveals all doors
        if i == carDoor:
            for j in range(0,3):
                if j == i:
                    print(doors[2])
                else:
                    print(doors[1])
            break
    if carDoor == originalDoor and switch == 0:
        print("Congratulations you won the car!")
        unswitchWin = unswitchWin + 1
    elif carDoor != originalDoor and switch == 1:
        print("Congratulations you won the car!")
        switchWin = switchWin + 1
    else:
        print("You lose, better luck next time.")
    print() #game stats displayed
    print("[Game Stats] Stayed: "+str(gamesPlayed-switchDoors)+" | Stayed&Win: "+str(unswitchWin)+" | Win: "+str(round(((unswitchWin/gamesPlayed)*100),1))+"%")
    print("             Switch: "+str(switchDoors)+" | Switch&Win: "+str(switchWin)+" | Win: "+str(round(((switchWin/gamesPlayed)*100),1))+"%")
    print()
    time.sleep(2)
    print("Play again?")
    while True: #loops until valid answer input
        userRepeat = int(input())
        if userRepeat != 1 and userRepeat != 0:
            print("Play again?")
        else:
            break
    if userRepeat == 0:
        keepPlaying = False
print("+++++++++++")

















