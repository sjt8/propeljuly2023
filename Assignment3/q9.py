# Rock-Paper-Scissors game

import random

user_score = 0
comp_score = 0


def compute_score(user, computer):
    global comp_score, user_score

    if user == computer:
        print("Draw")
    elif user == 1:
        if computer == 2:
            comp_score += 1
            print("1 point for computer")
        elif computer == 3:
            user_score += 1
            print("1 point for user")
    elif user == 2:
        if computer == 1:
            user_score += 1
            print("1 point for user")
        elif computer == 3:
            comp_score += 1
            print("1 point for computer")
    elif user == 3:
        if computer == 1:
            comp_score += 1
            print("1 point for computer")
        elif computer == 2:
            user_score += 1
            print("1 point for user")


def declare_winner(uscore, cscore):
    print("""
        Score
    """)
    if uscore < cscore:
        print("Computer Wins!!!")
        print("User Score: ", uscore)
        print("Computer Score: ", cscore)
    elif uscore > cscore:
        print("User Wins!!!")
        print("User Score: ", uscore)
        print("Computer Score: ", cscore)
    else:
        print("Draw")
        print("User Score: ", uscore)
        print("Computer Score: ", cscore)


def start_game():

    print("""
        Rock, Paper, Scissor
    """)

    chance = 10

    while chance > 0:
        chance -= 1
        print("\nChances Left:", chance)
        print("""
            1 - Rock
            2 - Paper
            3 - Scissor
        """)

        while True:

            computer = random.randrange(1, 4)
            user = input("Select an option from above: ")

            match user:
                case "1":
                    print("User:", user)
                    print("Computer:", computer)
                    compute_score(1, computer)
                    break
                case "2":
                    print("User:", user)
                    print("Computer:", computer)
                    compute_score(2, computer)
                    break
                case "3":
                    print("User:", user)
                    print("Computer:", computer)
                    compute_score(3, computer)
                    break
                case _:
                    print("Select from 1 to 3")

    declare_winner(user_score, comp_score)


start_game()
