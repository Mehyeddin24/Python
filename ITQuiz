gamerunning = True
score = 0
print("Welcome to the quiz!")
selection = input("Do you want to start to the quiz? ")
if selection.lower() == "yes":
    print("Ok, let's start!")
    gamerunning = True
else:
    print("Ok we're not starting now. Goodbye!")
    gamerunning = False

if gamerunning:
    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")

    answer = input("What does PSU stand for? ")
    if answer.lower() == "power supply":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")

    answer = input("What does RAM stand for? ")
    if answer.lower() == "random access memory":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")

    answer = input("What does IT stand for? ")
    if answer.lower() == "information technologies":
        print("Correct!")
        score = score + 1
        gamerunning = False
    else:
        print("Wrong!")
        gamerunning = False

    if gamerunning == False:
        if score < 4 and score > 0:
            print(f"Your score is {score}, not bad. But you need a little practice!")
        elif score == 4:
            print(f"Your score is {score}, you're perfect!")
        if score == 0:
            print(f"Your score is {score}. I guess you don't know any of these questions :(")
