def calculate_average(quizzes,activity,assignment):
    return (quizzes + activity + assignment) / 3

def calculate_grade(average):
    if average >=90:
        return 'A'
    elif average >=85:
        return 'B'
    elif average >=80:
        return 'C'
    elif average >=75:
        return 'D'
    else:
        return 'F'

while True:
    quizzes = float(input("Enter Quizzes Score : "))
    activity = float(input("Enter Activity Score : "))
    assignment = float(input("Enter Assignment Score : "))

    average = calculate_average(quizzes, activity, assignment)
    grade = calculate_grade(average)

    print(average)
    print(grade)

    choices = input("Would you like to compute again? yes or no :")
    if (choices == "no"):
        print("Thank you for using grade calculator")
        exit()