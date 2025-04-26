
import random
import string
import time

letters = list(string.ascii_uppercase) #creates a list of all the uppercase letters from A-Z
def levelup(difficulty, level):
    print("Level up!!")
    lvlup = level + 1
    if lvlup == 26:
        print("I didn't even think it was possible to win. Did you cheat? Either way, YOU WIN!!!")
    print("Level: " + str(lvlup))
    short = letters[:lvlup] #creates a shortened version of the alphabet with its length equal to their level
    scrambled = scramble(short) #scrambles that list
    play(difficulty, lvlup, scrambled) #calls the play function with the new level and new scrambled list
    
def Checker(string,level):
    for i in range(len(string)):
        if string[i] not in str(letters[:level]):
            return 1
    string = string.replace(" ", "").lower()#removes spaces and makes string lowercase
    total = 0
    for l in string:
        count = string.count(l) #checks if there are duplicates for every character in string
        if count > 1:
            total += count
    if total > 0:
        return 2
    else:
        return 3
        
def mastermind(): #This function is essentially just a menu where the player can select their difficulty
    print("Hi, welcome to Mastermind! Please select your difficulty:\n")
    difficulty = input("1: Easy\n2: Medium\n3: Hard\n4: Insane\n")
    if difficulty == "1":
        play(4, 1, letters[:1])
    if difficulty == "2":
        play(3, 1, letters[:1])
    if difficulty == "3":
        play(2, 1, letters[:1])
    if difficulty == "4":
        play(1, 1, letters[:1])
        
def scramble(list):
    seed = random.SystemRandom()
    scrambled = sorted(list, key = lambda x: seed.random() ) #sorts the list according to a random seed, effectively scrambling it
    return scrambled

def play(difficulty, level, scrambled): #This function is where most of the work is done
    for turn in range(difficulty): #Gives you an amount of turns based off of the previously selected difficulty
        print("Turns left: " + str(difficulty - turn))
        x = "" #this will be filled in to show which characters are correct and which aren't. It also clears itself after every guess
        print("Your options are: " + str(letters[:level]))
        guess = str.upper(input("guess the secret code: "))
        if len(guess) == len(scrambled):
            if Checker(guess, level) == 3: #these first 2 if statements check if there are duplicate characters and that the length is correct before continuing
                for i in range(len(scrambled)):#this loop compares each of the values of the secret and guess and at each index and appends and x or an o to x depending on if the values match
                    if guess[i] == scrambled[i]:
                        x += "X"
                    elif guess[i]!= scrambled[i]:
                        x += "O"
                if x == "X"*level: #checks if x is full of "X"s indicating that it is correct
                    print(guess + "\n" +x+ "\n")
                    levelup(difficulty, level) #calls levelup which rescrambles and adds another value to the list
                    return None
                else:
                    print(guess + "\n" +x)
            elif Checker(guess, level) == 2:
                print("Invalid option: Don't enter duplicate characters\nYou have been penalized 1 turn")
                time.sleep(2)
            elif Checker(guess, level) == 1:
                print("Invalid option: Please select a valid character\nYou have been penalized 1 turn")
                time.sleep(2)
        else:
            print("Invalid Option: Please enter " +str(level) + " characters\nYou have been penalized 1 turn")#these else statements are essentially just error codes
            time.sleep(2)
    print("Darn, you lost on level " + str(level) + " The answer was: " + str(scrambled)) #you lose message
    again = input("Play again?\n1: Yes\n2: No\n") #checks if you want to play again and calls play if you say yes
    if again == "1":
        play(difficulty, 1, letters[:1])
    else:
        print("Okay Cya!!")
            

mastermind() #calls the whole program
            