import random
number = random.randint(1,100)
guess = 0
attempts = 0
while guess != number:
    guess = int(input("Enter guess : "))
    attempts +=1
    if (guess < number):
        print("Higher Guess")
    elif (guess > number):
        print("Lower Guess")
    else:
        print("You guess it right", number)
print(f"You took {attempts} attempts to guess the right answer")

