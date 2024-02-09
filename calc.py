def add(x,y):
    return x+y
def minus(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y

a= int(input("Enter your number: "))
b= int(input("Enter second number: "))

function = input("What do you want to do, 'add', 'divide', 'minus' or 'multipy'")
if function == "add":
    print(add(x=a, y=b))
elif function == "minus":
    print(minus(x=a, y=b))
elif function == "multiply":
    print(multiply(x=a, y=b))
else:
    print(division(x = a, y = b))
    