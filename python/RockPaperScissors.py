import time
import random
print("Welcome to Rock Paper Scissors")
start = input("Do you want to start a game?: ")
while True:
    if start == "yes":
        run = True
        break
    elif start == "no":
        continue
    else:
        print("I don't understand that...")
hands = ["Rock", "Paper", "Scissors"]

def bot_choice():
    return random.choice(hands)


while run:
    for item in hands:
        print(item)

    while True:
        try:
            player_choice = input("Choose what to show")
        except player_choice == "n":
            pass
        
while run:
    for item in hands:
        print(item)
    try:
        x = int(input("Input a number: "))
    except ValueError:
        player_choice = ""
        print("Please input a number")
    
    if player_choice == 9:
        print("Correct")
        break
        
