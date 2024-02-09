def add(x,y):
    return x+y
def minus(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y

first_number = int(input("Enter your first number: "))
function = input("What do you want to do:\n +\n -\n *\n /\n")
second_number = int(input("Enter your second number: "))

def calculation():
    if function == "+":
        print(add(x=first_number, y=second_number))
    elif function == "-":
        print(minus(x=first_number, y=second_number))
    elif function == "*":
        print(multiply(x=first_number, y=second_number))
    else:
        print(division(x=first_number, y=second_number))
calculation()


