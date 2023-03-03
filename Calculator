import time
run = True
while run:
    operation = input("Enter the operation: addition(+), subtraction(-),multiplication(*),division(/): \nEnter here: ")
    if operation == "/" or operation.lower() == "divison":
        choise = input("If you want to change the operation just write back:")
        if choise.lower() == "back":
            continue
        print("Ok, let's start")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(f"Final result is {a/b}")
    elif operation == "+" or operation.lower() == "addition":
        choise = input("If you want to change the operation just write back, else write smth except back: ")
        if choise.lower() == "back":
            continue
        else:
            print("Ok, let's start")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(f"Final result is {a+b}")
    elif operation == "*" or operation.lower() == "multiplication":
        choise = input("If you want to change the operation just write back, else write smth except back: ")
        if choise.lower() == "back":
            continue
        else:
            print("Ok, let's start")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(f"Final result is {a * b}")
    elif operation == "-" or operation.lower() == "subtraction":
        choise = input("If you want to change the operation just write back, else write smth except back: ")
        if choise.lower() == "back":
            continue
        else:
            print("Ok, let's start")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(f"Final result is {a-b}")
    else:
        print("You entered wrong command. Shutting down.")
        time.sleep(3)
        break
    print("-----------------------------------------")
    answer = input("You got your result. So, do you want to calculate again? \nEnter here: ")
    if answer.lower() == "yes":
        continue
    else:
        print("Ok, see you soon :>")
        time.sleep(4)
        run = False
