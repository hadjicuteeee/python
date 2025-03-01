def add():
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    return num1+num2

def subtract():
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    return num1 - num2

def multiply():
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    return num1 * num2

def divide():
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    if num2== 0:
        return 'Error'
    return num1 / num2


while True:
    operator = input( "1. Add 2.Subtract 3. Multiply 4. Divide 5.Exit  : ")
    if operator == "5":
        print("Thank you for using calculator")
        exit()
    if operator == "1":
        print("The sum is ", add())
    elif operator =="2":
        print("The difference", subtract())
    elif operator =="3":
        print("The product is", multiply())
    elif operator =="4":
        print("The quotient is", divide())
    else:
        print("No operators found")