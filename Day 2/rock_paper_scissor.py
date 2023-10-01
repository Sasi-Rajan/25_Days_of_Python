rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
images=[rock,paper,scissors]
computer=random.randint(0,2)
user=int(input("Enter 0 for rock, 1 for paper and 2 for scissors "))
if user < 3 and user >= 0:
  print(f"computer choose {computer}")
  print(images[computer])
  print(f"You choose {user}")
  print(images[user])
  if user == computer:
    print("Match Draw!")
  if computer == 0 and user == 1:
    print("You win!")
  elif computer == 0 and user == 2:
    print("You lost")
  elif computer ==1 and user ==0:
    print("You lost")
  elif computer ==1 and user ==2:
    print("You win")
  elif computer == 2 and user == 0:
    print("You win")
  elif computer == 2 and user == 1:
    print("You lost")

else:
  print("You entered wrong number! You lose")
