print("Welcome to the club")
age = int(input("Enter age: "))
mem = input(f"Are you a member yes/no: ")
vip = input(f"Are you a vip? yes/no: ")
if age >= 18 and mem =="no" and vip == "no":
    print("Sorry, but you are not allowed to enter")
elif age >= 18 and mem == "yes" and vip =="no":
    print("Welcome, member!")
elif age >= 18 and mem =="no" and vip =="yes":
    print("Welcome, Vip!")
elif age >= 18 and mem =="yes" and vip =="yes":
    print("Welcome, Boss!")
else:
    print("Sorry, but you are not allowed to enter")