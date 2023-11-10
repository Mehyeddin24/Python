import random
import time

gameRunning = True
compscore = 0
score = 0

print("Best of 3 - Rock, Paper Scissors:")
while True:
    options = ["rock", "paper", "scissors"]
    selection = input("Choose one: ROCK, PAPER OR SCISSORS? \nYou choose: ")
    print("----------------------------------------------------------------")
    comp_input = random.choice(options)
    if selection.lower() == "rock":
        if comp_input == "rock":
            print("You chose: Rock")
            print("Computer chose: Rock")
            print("TIE!")
            print("----------------------------------------------------------------")
        elif comp_input == "paper":
            print("You chose: Rock")
            print("Computer chose: Paper")
            print("COMPUTER WINS!")
            print("----------------------------------------------------------------")
            compscore = compscore + 1
        else:
            print("You chose: Rock")
            print("Computer chose: Scissors")
            print("YOU WIN!")
            print("----------------------------------------------------------------")
            score = score + 1

    elif selection.lower() == "paper":
        if comp_input == "rock":
            print("You chose: Paper")
            print("Computer chose: Rock")
            print("YOU WIN!")
            print("----------------------------------------------------------------")
            score = score + 1
        elif comp_input == "paper":
            print("You chose: Paper")
            print("Computer chose: Paper")
            print("TIE!")
            print("----------------------------------------------------------------")
        else:
            print("You chose: Paper")
            print("Computer chose: Scissors")
            print("COMPUTER WINS!")
            print("----------------------------------------------------------------")
            compscore = compscore + 1

    elif selection.lower() == "scissors":
        if comp_input == "rock":
            print("You chose: Scissors")
            print("Computer chose: Rock")
            print("COMPUTER WINS!")
            print("----------------------------------------------------------------")
            compscore = compscore + 1
        elif comp_input == "paper":
            print("You chose: Scissors")
            print("Computer chose: Paper")
            print("YOU WIN!")
            print("----------------------------------------------------------------")
            score = score + 1
        else:
            print("You chose: Scissors")
            print("Computer chose: Scissors")
            print("TIE")
            print("----------------------------------------------------------------")
    if compscore == 3:
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxx GAME OVER xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        break
    elif score == 3:
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxx YOU WIN xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        break
