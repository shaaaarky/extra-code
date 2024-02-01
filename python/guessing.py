import random
import time
# Number guessing range
guess_sizes = [10, 20, 50, 100 ]
guess_max = random.choice(guess_sizes)
guess_sizes.remove(guess_max)
guess_min = random.choice(guess_sizes)
# Number picked
number_picked = random.randint(guess_min, guess_max)
# Welcome message and player's guess
def timer(s):
    while True:
        print("...")
        time.sleep(1)
        s -= 1
        if s == 0:
            break
while True:
    wins = 0
    tries = 3
    print("Welcome to number guess! Made by sharky")
    print(f"Pick a number from {guess_min} to {guess_max}")
    
    # if you input a word, the program is going to crash so instead,
    # we ask the user to input again
    try:
        guessed_number = int(input("#: "))
    except ValueError:
        guessed_number = ""
        print("(Please input a number)")
    
    
    
    if guessed_number == number_picked:
        wins += 1
        print("Correct! You win!")
        break
    elif guessed_number != number_picked:
        tries -= 1

    if tries == 0:
        while True:
            print("You don't have any tries left! Want to generate a new number")
            regen_number = input("# ")
            regen_number.lower
            if regen_number == "y":
                timer(s= 3)
                break
            elif regen_number == "n":
                exit
            else:
                print("I don't understand that...")
                break
    elif tries >= 1:
        print(f"Incorrect. You have {tries} more tries ")



