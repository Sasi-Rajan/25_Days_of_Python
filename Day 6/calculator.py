from art import logo
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operation={"+":add,"-":subtract,"*":multiply,"/":divide}
def calculator():
    print(logo)
    num1=float(input("Enter first number "))
    for key in operation.keys():
        print(key)
    result=False
    while not result:
        operation_symbol=input("Pick an operation ")
        num2=float(input("Enter next number "))
        calculation=operation[operation_symbol]
        answer=calculation(num1,num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue with {answer}: or 'n' to exit for new calculation ")=="y":
            num1=answer
        else:
            result=True
            calculator()
calculator()
