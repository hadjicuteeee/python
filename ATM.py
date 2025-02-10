balance = 5000
deposit = balance

while True:
    print("Welcome to ATM simulator")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


    choices = int(input("Enter your choices : "))
    if (choices == 4):
        print("Thank you for using ATM SIMULATOR")
        exit()
    if (choices == 1):
        print("Your current balance is", balance)
    elif (choices == 2):
        deposit = float(input("Enter amount to deposit : "))
        balance += deposit
        print(balance)
    elif (choices == 3):
        amount = float(input("Enter amount to withdraw : "))
        if (amount < balance):
            balance = balance - amount
            print("Success")
            print("Total balance", balance)
        elif (amount > balance):
            print("Insufficient balance your total balance is", balance)



