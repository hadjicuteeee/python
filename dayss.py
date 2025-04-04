def monday():
    return 'Monday'

def tuesday():
    return 'Tuesday'

def wednesday():
    return 'Wednesday'

def thursday():
    return 'Thursday'

def friday():
    return 'Friday'

def saturday():
    return 'Saturday'


def sunday():
    return 'Sunday'


print("Days Converter")

while True:
    converter = input("Enter days you want to convert :")
    if converter == "Exit":
        exit()
    if converter =="1":
        print("Today is", monday())
    elif converter =="2":
        print("Today is", tuesday())
    elif converter =="3":
        print("Today is", wednesday())
    elif converter =="4":
        print("Today is", thursday())
    elif converter =="5":
        print("Today is", friday())
    elif converter =="6":
        print("Today is", saturday())
    elif converter =="7":
        print("Today is", sunday())
    else:
        print("No days found")




