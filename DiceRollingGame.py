import random

gameRunning = True

while gameRunning:
    answer = input("Welcome to the Dice Rolling Game is here for you! Wanna start? [Yes/No] \nEnter here: ")
    if answer.lower() == "yes":
        comp = random.randint(1,6)
        player = random.randint(1,6)
        print(f"You rolled {player}, and the computer rolled {comp}")
        if player > comp:
            print("+ + + Player WON! + + +")
        elif player == comp:
            print("x x x It's a tie! x x x")
        else:
            print("- - - Computer WON! - - -")
        choise = input("Wanna play again? :> [Yes/No]\nEnter here: ")
        if choise.lower() == "yes":
            print("-----------------------------------")
            continue
        else:
            print("Ok, see you soon! :>")
            break
    else:
        print("Ok, see you soon! :>")
        exit()
