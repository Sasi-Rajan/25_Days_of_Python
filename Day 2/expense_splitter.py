print("Welcome to the tip calculator")
total_bill=float(input("What was the total bill? "))
tip=int(input("What percentage tip would you like to give 10 , 12 , 15 "))
members=int(input("How many members going to split the bill "))
percentage=(total_bill/100)*tip
split=(total_bill+percentage)/members
final_amount="{:.2f}".format(round(split,2))
print("Each should need to pay ",final_amount)