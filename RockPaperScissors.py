import random
import time

print(("-"*30) + "\nRock, Paper, Scissors\n" + ("-" * 30))

user_score, computer_score = 0, 0
computer_game_change = 3
user_game_change = 3
while True:
    print("\n1- Rock\n2- Paper\n3- Scissors")
    user_choice = input("Your choice: ")
    computer_choice = random.choice(["1","2","3"]) # random choice takes a list or set, etc.
    if user_choice == "1":
        if computer_choice == "1":
            time.sleep(1)
            print("Computer's choice: Rock\nRock equal to rock, Scoreless!")
        elif computer_choice == "2":
            time.sleep(1)
            print("Computer's choise: Paper\nPaper wraps stone, You lose!")
            user_game_change -= 1
            computer_score += 100
        elif computer_choice == "3":
            time.sleep(1)
            print("Computer's choise: Scissors\nRock breaks scissors, You win!")
            computer_game_change -= 1
            user_score += 100
    elif user_choice == "2":
        if computer_choice == "1":
            time.sleep(1)
            print("Computer's choice: Rock\nPaper wraps stone, You win!")
            computer_game_change -= 1
            user_score += 100
        elif computer_choice == "2":
            time.sleep(1)
            print("Computer's choice: Paper\nPaper equal to paper, Scorless!")
        elif computer_choice == "3":
            time.sleep(1)
            print("Computer's choice: Scissors\nScissors cuts paper, You lose!")
            user_game_change -= 1
            computer_score += 100
    elif user_choice == "3":
        if computer_choice == "1":
            time.sleep(1)
            print("Computer's choice: Rock\nRock breaks scissors, You lose!")
            user_game_change -= 1
            computer_score += 100
        elif computer_choice == "2":
            time.sleep(1)
            print("Computer's choice: Paper\nScissors cuts paper,You win!")
            computer_game_change -= 1
            user_score += 100
        elif computer_choice == "3":
            time.sleep(1)
            print("Computer's choice: Scissors\nScissors equal to scissors, Scoreless!")
    elif not 1<=int(user_choice)<=3:
        print("Wrong choice, Try again!")

    print("User game change: {}\nComputer game change: {}".format(user_game_change, computer_game_change))

    if computer_game_change == 0:
        print("\nGame over!\nYou win!\nComputer lose!")
        print("\nUser's score: {}\nComputer's score: {}".format(user_score,computer_score))
        break
    if user_game_change == 0:
        print("\nGame over!\nComputer win!\nYou lose!")
        print("\nUser's score: {}\nComputer's score: {}".format(user_score,computer_score))
        break
    print("\nUser's score: {}\nComputer's score: {}".format(user_score,computer_score))