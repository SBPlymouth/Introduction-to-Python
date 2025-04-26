# import random module
import random
import time


# Print multiline instruction
# performstring concatenation of string
print("Winning Rules of the Rock paper scissor game as follows: \n"
								+"Rock vs paper->paper wins -> Paper covers Rock\n"
								+ "Rock vs scissor->Rock wins -> Rock crushes Scissors\n"
								+"paper vs scissor->scissor wins -> Scissors cuts Paper\n")

while True:
    print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
	
	# take the input from user
    choice = int(input("User turn: "))

	# OR is the short-circuit operator
	# if any one of the condition is true
	# then it return True value
	
	# looping until user enter invalid input
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))
		

	# initialize value of choice_name variable
	# corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
		
	# print user choice
    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")
    print()
    time.sleep(2)

	# Computer chooses randomly any number
	# among 1 , 2 and 3. Using randint method
	# of random module
    comp_choice = random.randint(1, 3)
	
	# looping until comp_choice value
	# is not equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

	# initialize value of comp_choice_name
	# variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'
		
    print("Computer choice is: " + comp_choice_name)
    time.sleep(1)

    print(choice_name + " V/s " + comp_choice_name)
    time.sleep(1)
	
	# condition for winning
    if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice ==1 )):
        print("paper wins => Paper covers Rock ", end = "")
        result = "paper"

    elif((choice == 1 and comp_choice == 3) or
	(choice == 3 and comp_choice == 1)):
        print("Rock wins => Rock crushes Scissors ", end = "")
        result = "Rock"
    else:
        print("scissor wins => Scissors cuts Paper ", end = "")
        result = "scissor"

	# Printing either user or computer wins or draw
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
		
    time.sleep(2)
    ans = input("Do you want to play again? (Y/N):")


	# if user input n or N then condition is True
    if ans.lower() == 'n':
        break
	
# after coming out of the while loop
# we print thanks for playing
print("\nThanks for playing")
