import random
import time

history = []

ai = input("hello!\n")

wins = 0
ties = 0
loses = 0


def game_number(wins, loses, history, name):
    history.append(f"{name} played (number guessing game)")
    time.sleep(1)
    print("let's start right now!")
    time.sleep(1)
    print("loading game...")
    time.sleep(5)

    while True:

        print("\n================")
        print("guess the number")
        print("================\n")

        secret_num = random.randint(1, 100)

        lifes = 5

        while True:
            try:
                guess = int(input(f"guess a number between 1 and 100 you have {lifes} lifes!\n"))
            except:
                print("pls pick a number")
                continue

            if guess < 1 or guess > 100:
                print("pls pick a number between 1 and 100")
                lifes -= 1
                print(f"lifes left {lifes}")

            elif guess < secret_num:
                print("too low!")
                lifes -= 1
                print(f"lifes left {lifes}")

            elif guess > secret_num:
                print("too high!")
                lifes -= 1
                print(f"lifes left {lifes}")

            else:
                print(f"correct good job {name}!")
                history.append(f"{name} won in (guess the number)")
                wins += 1
                break

            if lifes <= 0:
                print(f"you lost the number was {secret_num}")
                history.append(f"{name} lost in (guess the number)")
                loses += 1
                break

        again = input("wanna play again?\n")
        if again.strip().lower() not in ["yes", "sure", "yea", "y"]:
            print("ok bye!")
            break

    return wins, loses


if ai.strip().lower() in ["hello", "hi"]:
    name = input("hi! what is your name?\n")
    print(f"welcome {name} i am your ai assistant!")
else:
    print("i dont understand?")
    name = "unknown_user"


game = input("wanna play a game?\n")

if game.strip().lower() in ["yes", "yea", "sure", "y"]:
    print(f"ok that sounds good {name}!")

    time.sleep(1)
    while True:
        print("\n===================")
        print("       menu       ")
        print("===================\n")

        what_play = input(
            "what do you wanna play\n"
            "1: guess the number!\n"
            "2: rock paper scissors\n"
            "3: history\n"
            "4: stats\n"
            "5: quit\n"
        )

        if what_play == "1":
            wins, loses = game_number(wins, loses, history, name)

        elif what_play == "2":
            history.append(f"{name} played (rock paper scissors)")
            print("ok")
            time.sleep(1)
            print("loading game...")
            time.sleep(5)

            while True:
                print("\n==============")
                print("     rps     ")
                print("==============\n")

                bot = random.choice(["rock", "paper", "scissors"])
                choice = input("what do you choice?\n")

                if choice not in ["paper", "rock", "scissors"]:
                    print("pls pick (rock paper scissors)")

                print(f"ai choice {bot}!")

                if choice == "rock" and bot == "scissors" or \
                   choice == "paper" and bot == "rock" or \
                   choice == "scissors" and bot == "paper":

                    again_2 = input("you win! play again?\n")
                    wins += 1
                    history.append(f"{name} has won (rock paper scissors)")

                    if again_2.strip().lower() not in ["yes", "y", "sure", "yea"]:
                        print("ok byeee!")
                        break

                elif choice == bot:
                    again_4 = input("tie! play again?\n")
                    ties += 1
                    history.append(f"{name} has tied in (rock paper scissors)")

                    if again_4.strip().lower() not in ["yes", "y", "sure", "yea"]:
                        print("ok byeee!")
                        break

                else:
                    again_3 = input("you lose play again?\n")
                    loses += 1
                    history.append(f"{name} has lost in (rock paper scissors)")

                    if again_3.strip().lower() not in ["yes", "y", "sure", "yea"]:
                        print("ok byeee!")
                        break

        elif what_play == "3":
            print("=============")
            print("   history   ")
            print("=============\n")

            if len(history) == 0:
                print("no history yet\n")
            else:
                for items in history:
                    time.sleep(1.5)
                    print(f"{items}\n")

        elif what_play == "4":
            print("\n=================")
            print("      stats      ")
            print("=================\n")

            history.append(f"{name} went to stats")
            time.sleep(1)

            if wins == 0 and loses == 0 and ties == 0:
                print("no stats yet")
                time.sleep(1.5)
            else:
                print(f"wins: {wins}")
                print(f"losses: {loses}")
                print(f"ties: {ties}")
                time.sleep(1.5)

        elif what_play == "5":
            print("bye bye :)")
            history.append(f"{name} has left")
            break

elif game.strip().lower() in ["no", "nah", "nope"]:
    print("oh that's ok!")
else:
    print("i dont understand?")