import random

computer_guess=random.randint(1,10)

guess=0
player_name=input("Enter your name:")

print(f"OK...! let play {player_name} let's the Number")



while guess<5:
    player_guess=int(input("Enter the gussing number:"))
    guess+=1
    if player_guess < computer_guess:
        print("it to low")
    if player_guess > computer_guess:
        print("it to high")
    if player_guess == computer_guess:
        break
if player_guess==computer_guess:
    print(f"you guess is right {player_guess} you  win")
else:
    print(f"you can't guess the number {computer_guess} you lose..")
    
    