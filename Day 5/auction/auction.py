import os
from art import logo
print(logo)
over = True
bidding={}
winner=0
name=""
while over:
  name=input("Enter your name ")
  amount=int(input("Enter amount to bid in rs: "))
  bidding[name]=amount
  os.system("cls" if os.name == "nt" else "clear")
  user_val=input("Are there any other bidders y/n ").lower()
  if user_val=="n":
    over=False
    for key , values in bidding.items():
      if values > winner:
        winner = values
        name=key
    print("The winner is {0} with a bid of {1}".format(name,winner))
        