import random
name_database = ["sharky"]
total_card_value = 0
card_count = 1
# [placeholder] (put actual deck and probability here)
card_selection = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
card_suit_selection = ["♠", "♥", "♣", "♦", "♤", "♡", "♧", "♢"]
letter_card_values = {
    "Ace": 1,
    "J": 10,
    "Q": 10,
    "K": 10
}
card_text = {
    1: "First Card:",
    2: "Second Card:",
    3: "Third Card:",
    4: "Fourth Card: ",
    5: "Fifth Card:",
    6: "Sixth Card:",
    7: "Seventh Card:",
    8: "Eight Card: ",
    9: "Ninth Card: ",
    10: "Tenth card: "
}
name = input("Name: ").lower()
if name in name_database:
    # Basic gameplay loop
    run = input("Welcome to blackjack! Want to play a game? Y/N: ").lower()
    if run == "yes":
        for item in range(2):
            try:
                deck_choice = random.choice(card_selection)
                card_suit = random.choice(card_suit_selection)
                print(f'{card_text[card_count]} {deck_choice}{card_suit}')
                card_count += 1
                if type(deck_choice) is str:
                    total_card_value += letter_card_values[deck_choice]
                else:
                    total_card_value += deck_choice
            except KeyError:
                print("Not enough card introductions have been written! ")
                exit()
        while total_card_value < 21:
            extra_card = input("Want another card? Y/N: ").lower()
            if extra_card == "yes":
                try:
                    deck_choice = random.choice(card_selection)
                    print(f'{card_text[card_count]} {deck_choice}')
                    card_count += 1
                    if type(deck_choice) is str:
                        total_card_value += letter_card_values[deck_choice]
                    else:
                        total_card_value += deck_choice
                # Ignores Key_Error errors of having not enough card ordinals
                except KeyError:
                    print("Not enough card introductions have been written in the code ")
                    exit()
                if total_card_value > 21:
                    print("You've gone bust! Thanks for playing")
                    exit()
            elif extra_card == "no":
                print("Wait for ur turn")
                break
            if total_card_value == 21:
                print("Congrats! You win!")
                break
            if total_card_value > 21:
                print("You've gone bust! Thanks for playing")
                break
    elif run == "no":
        print("Ok. Have a good day!")
        exit()
    else:
        print("I don't understand that")
else:
    print("Username not found!")
