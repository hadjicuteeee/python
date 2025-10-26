lives = 3
answer = "jihad"
print("What is the name of user?")

while lives > 0:
    ans = input("Type your answer here : ")
    if ans == answer:
        print("You are korique")
        break
    else:
        lives = lives - 1
else:
    print("You lost")
