import random

chose=["rock","papper","sicross"]

computer=random.choice(chose)
player=None
while player not in chose:
    player=input("rock , papper , sicross :")

    if player == computer:
        print("your choose:",player)
        print("computer choose:",computer)
        print("Tird")
    elif player=="rock":
        if computer=="papper":
            print("your choose:", player)
            print("computer choose:", computer)
            print("you lose")
        if computer=="rock":
            print("your choose:", player)
            print("computer choose:", computer)
            print("Tird")
        if computer=="sicross":
            print("your choose:", player)
            print("computer choose:", computer)
            print("you win")
    elif player == "papper":
            if computer == "papper":
                print("your choose:", player)
                print("computer choose:", computer)
                print("Tird")
            if computer=="rock":
                print("your choose:", player)
                print("computer choose:", computer)
                print("you win")
            if computer=="sicross":
                print("your choose:", player)
                print("computer choose:", computer)
                print("you lose")
    elif player=="sicross":
            if computer=="rock":
                print("your choose:", player)
                print("computer choose:", computer)
                print("you lose")
            if computer=="papper":
                print("your choose:", player)
                print("computer choose:", computer)
                print("you win")
            if computer=="sicross":
                print("your choose:", player)
                print("computer choose:", computer)
                print("Tird")
    player=input("do yo want to play again(Y/N):")
