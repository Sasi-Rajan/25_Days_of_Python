from art import logo , vs
from game_data import data
import random
import os
score=0
game_start=True

def format_data(account):
    """Take the account data and return the data into printabe one"""
    acc_name=account["name"]
    acc_description=account["description"]
    acc_country=account["country"]
    return f"{acc_name} , a {acc_description} , from {acc_country}"



def check_answer(guess,a_follower_count,b_follower_count):
    """Take user guess and follower count and return if they got right"""
    if a_follower_count > b_follower_count:
        if guess == "a":
            return True
        else:
            return False
    if  b_follower_count > a_follower_count:
        if guess == "b":
            return True
        else:
            return False
            
    
# display art
print(logo)
acc_b=random.choice(data)

#make create repeatable
while game_start:
# Generate random account from the game data

    #making account at position B become the next account at position A
    acc_a=acc_b
    acc_b=random.choice(data)
    while acc_a == acc_b:
        acc_b=random.choice(data)
    print(f"Compare A: {format_data(acc_a)}")
    print(vs)
    print(f"Against B: {format_data(acc_b)}")
    # Ask user guess
    guess=input("Who has more followers? Type 'A' or 'B' ").lower()
    # Check if user is correct
    # Get follower count of each account
    a_follower_count=acc_a["follower_count"]
    b_follower_count=acc_b["follower_count"]
    is_correct=check_answer(guess,a_follower_count,b_follower_count)
    os.system("cls" if os.name=="nt" else "clear")
    print(logo)

    if is_correct:
        score+=1
        print(f"You're right. Current score {score}")
    else:
        game_start=False
        print(f"You're wrong. Final score {score}")
