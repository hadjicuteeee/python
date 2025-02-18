bg = {
    "height":55,
    "weight":53
}


studentOne = {
    "name":"Jihad Apues",
    "course":"BSIT",
    "age": 20,
    "apperances": bg
}

studentTwo = {
    "name":"Lei Quirimit",
    "course":"BSIT",
    "age": 22
}

studentThree = {
    "name":"Matthew Palileo",
    "course":"BSIT",
    "age": 22
}

studentFour = {
    "name":"Rejie Cellacay",
    "course":"BSIT",
    "age": 19
}

studentFive = studentOne.copy()
studentFive["name"] = "Luve Bacuyong"

studentSix = studentFour.copy()
studentSix["name"] = "Angelique Jamille"

studentSeven = {
    "name":"Kent Apable",
    "course":"BSIT",
    "age": 21
}

studentEight = studentOne.copy()
studentEight["name"] = "Eumi Bituin"
studentEight["age"] = 21

studentOne["name"] = "Jihad Dion Apues"

students = [studentOne,studentTwo,studentThree,studentFour,studentFive,studentSix,studentSeven,studentEight]

for i, student in enumerate(students, start=1):
    print(f"Student {i}")
    for key, value in student.items():
        print(f"{key}: {value}")
    print()


#for value in studentEight.values():
    #print("Name: ",value)


#print(studentFive)
#print(studentSix)