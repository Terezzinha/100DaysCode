
## Display logo game
import art
print(art.logo_higher_lower)

def format_data(f_data):
    """Format the account data into printable format"""
    nome = f_data['name']
    follower = f_data['follower_count']
    description = f_data['description']  
    country = f_data['country']

    return(f"{nome}, {description}, from {country} ")


def get_followers(f_data):
    """Get the number of follewer of Instagram account"""
    follower = f_data['follower_count']
    return follower

def check_answer (user_guess, followersA, followersB):
    """Return if user guess is correct"""
    if followerA > followerB:
        return user_guess == "A"
    elif followersB > followersA:
        return user_guess == "B"
        

# Generate a random account from the game data.
import random
from day14_data_higher_lower import data

diceA = random.choice(data)
diceB = random.choice(data)
if diceA == diceB:
    diceB = random.choice(data)

is_correct = True
score = 0

while is_correct:
    print(f"Compare A: {format_data(diceA)}" ) 
    print("VS")
    print(f"Compare B: {format_data(diceB)}" ) 
    print('--------------------------------')

    followerA = get_followers(diceA)
    followerB = get_followers(diceB)

    answer = input ("> Who has mores followers on Instagram? A ou B:" ).upper()
    
    is_correct = check_answer(answer, followerA, followerB)
    if is_correct:
        score += 1
        print(f"You right! Your scores is {score}")
    else:
        print(f"You lose! Final score {score}")
    
    print(f"A has {get_followers(diceA)}")
    print(f"B has {get_followers(diceB)}")
   
    diceA = diceB
    diceB = random.choice(data)

    print('--------------------------------')
