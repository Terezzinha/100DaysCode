
import art
## Print logo game
print(art.logo_higher_lower)

def format_data(f_data):
    nome = f_data['name']
    follower = f_data['follower_count']
    description = f_data['description']  
    country = f_data['country']

    print(f"{nome}, {description}, from {country} ")


def get_followers(f_data):
    follower = f_data['follower_count']
    return follower

# Generate a random account from the game data.
import random
from day14_game_data_higher_lower import data

diceA = random.choice(data)
diceB = random.choice(data)

still_win = True

while still_win:
    # Format account data into printable format.
    format_data(diceA)
    print("VS")
    format_data(diceB)
    print('--------------------------------')

    followerA = get_followers(diceA)
    followerB = get_followers(diceB)

    answer = input ("Who has mores followers on Instagram? A ou B: " )

    if (answer == "A") and (followerA > followerB):
        print("You win")
    elif (answer == "B") and (followerA < followerB):
        print("You win")
    else:
        print("You lose")    
        still_win = False
        
    diceA = diceB
    diceB = random.choice(data)
    print('--------------------------------')
#
# # Load game data 


## print("oi")

## Choose a random number
 

### Pick Dice01
### print Vs logo
### Pick Dice02

## Show Dice01
## Show Dice02

## Ask the user who has higher number Instagram follow  


######## Angela algorithm
# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.
