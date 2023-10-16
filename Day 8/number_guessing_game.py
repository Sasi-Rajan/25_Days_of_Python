import random
from ascii import logo
print(logo)


#number guessing function                
def number_guessing():
    print("Welcome to the number guessing game!")
    print("Im thinking number between 1 to 100")
    global computer_choice
    computer_choice=random.randint(1,100)
    print(f"The correct answer is {computer_choice}")
    level=input("Choose a difficulty. Type easy or hard ").lower()
    if level == "easy":
        easy()
    elif level == "hard":
        hard()



# for easy game
def easy():
    print("You have 10 attempt to guess the game make a guess ")
    attempt=10
    while attempt != 0:
        user_input=int(input("Make a guess "))
        if user_input == computer_choice:
            print(f"You got it. The answer is {computer_choice}")
        else:
            attempt -= 1
            print(f"You have {attempt} guess left")
            if attempt == 0:
                print("You lose")
            elif user_input > computer_choice:
                print("Guess lower")
            elif user_input < computer_choice:
                print("Guess higher")                
                
                

#for hard game
def hard():
    print("You have 5 attempt to guess the game make a guess ")
    attempt=5
    while attempt != 0:
        user_input=int(input("Make a guess "))
        if user_input == computer_choice:
            print(f"You got it. The answer is {computer_choice}")
        else:
            attempt -= 1
            print(f"You have {attempt} guess left")
            if attempt == 0:
                print("You lose")
            elif user_input > computer_choice:
                print("Guess lower")
            elif user_input < computer_choice:
                print("Guess higher")                
                
#calling the function                
number_guessing()       

