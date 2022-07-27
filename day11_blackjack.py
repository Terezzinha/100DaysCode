import random
## sincronization by git
##################### Hints #####################
# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#BLACKJACK = 21
ACE = 11


def deal_card(cards_player, amout_cards):
    """Distribui as cartas para os jogadores"""
    for i in range(0, amout_cards):
        cards_player.append(random.choice(cards))


def calculate_score(cards_player):
    """Calcula a pontuação de cada jogador"""
    score = sum(cards_player)
    if len(cards_player) == 2 and score == 21:
        if ACE in cards_player and 10 in cards_player:
            score = 0
            return score

    if score > 21:
        if ACE in cards_player:
            # remove ace
            cards_player.romove(ACE)
    score = sum(cards_player)
    return score


######
computer_cards = []
user_cards = []
deal_card(computer_cards, 2)
deal_card(user_cards, 2)
print(f"computer cards {computer_cards}. User cards {user_cards}")

computer_score = calculate_score(computer_cards)
user_score = calculate_score(user_cards)
print(f"computer score {computer_score}. User score {user_score}")

if user_score == 0 or computer_score == 0:
    print(f"Game over. Blackjack")
else:
    another_card = input("Do want another card? (y/n):")
    if another_card == "y":
        deal_card(user_cards, 1)
        user_score = calculate_score(user_cards)
        print(user_cards, user_score)

    if user_score <= 21 and user_score > computer_score:
        print("YOU WIN!")
    else:
        print("You looose")

# print(computer_cards)
