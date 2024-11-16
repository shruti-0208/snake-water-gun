#  PROJECT  : "Snake, Water, Gun Game"

import random

name = input("Player's name: ")
print(f"\nWELCOME {name}\n\nLet's play\nSnake, Water, or Gun\n\n:INSTRUCTIONS:\n\nSnake wins over Water\nWater wins over Gun\nGun wins over Snake\n\nGame is between 2 players:\n{name} v/s Python\n\nWhoever scores 5 points first wins the game\n")

def gameWin(P, C):
    a = random.randint(1, 3)
    if a == 1:
        comp = 's'
    elif a == 2:
        comp = 'w'
    else:
        comp = 'g'

    print("Python has choosen!")
    you = input(f"{name} chose: Snake(s), Water (w), or Gun (g)? ").lower()
    print(f"Python: {comp}, {name}: {you}")
    
    if comp == you:
        print("Tie!")
        # print(f"SCORES:\n{name}: {P} and Python: {C}")
    
    elif comp == 's':
        if you == 'w':
            C += 1
        elif you == 'g':
            P += 1
    
    elif comp == 'w':
        if you == 'g':
            C += 1
        elif you == 's':
            P += 1
    
    elif comp == 'g':
        if you == 's':
            C += 1
        elif you == 'w':
            P += 1

    print(f"SCORES:\n{name}: {P} and Python: {C}\n")
    return P, C

def play():
    P, C = 0, 0
    while P < 5 and C < 5:
        P, C = gameWin(P, C)
    if P == 5:
        print(f"{name} wins the game!")
    else:
        print("Python wins the game!")

play()
choice = input("Do you want to play again? Press 'y' for yes and any key to exit: ").lower()
while choice == 'y':
    play()
    choice = input("Do you want to play again? Press 'y' for yes and any key to exit: ").lower()
if choice!='y':
    print("Thankyou for playing!")


