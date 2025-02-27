def summatationOf(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

print(summatationOf(1,2,3,4,5,6))
