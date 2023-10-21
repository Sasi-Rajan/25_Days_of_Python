from art import coffee_logo
from resources import menu , resources
machine_on=True
profit=0

def is_resources_sufficicent(order_ingredients):
    """Return true if order ingredients are sufficient in resources"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True    



def process_coins():
    """Return the total calculated from inserted coins"""
    print("Please insert coins")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickels?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total
    



def is_transaction_successful(money_received,drink_cost):
    """Return True when payment is accepted or False if not enough money"""
    if money_received >= drink_cost:
        change=round(money_received - drink_cost,2)
        print(f"Here is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("You dont have enough money. Your money is refunded")
        return False

def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Have your {coffee_logo} {drink_name}")



while machine_on:
    user_input=input(("What would you like? (espresso/latte/cappuccino): ")).lower()
    

    if user_input == "off":
        machine_on=False
        

    elif user_input == "report":
        print(f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']} \nMoney: {profit}")
    
    else:
        drink = menu[user_input]
        if is_resources_sufficicent(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(user_input,drink["ingredients"])