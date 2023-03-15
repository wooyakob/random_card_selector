import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand =[]


# While List to iterate as long as the diamonds lists is not empty
while diamonds:
    user_choice = input("type P to pick a card, or type Q to Quit: ")
    print("\n\n")
    if user_choice == "Q":
        break
    if user_choice == "P":
        random_card = random.choice(diamonds)
        print("Your hand: " , random.choice(diamonds))
        print("\n\n")
        diamonds.remove(random_card)
        hand.append(random_card)
        print("Remaining cards: " , diamonds[:])
        print("\n\n")
    else:
        print("Invalid choice, please type either P or Q!")
        print("\n\n")

if not diamonds:
    print("There are no more cards to pick!")