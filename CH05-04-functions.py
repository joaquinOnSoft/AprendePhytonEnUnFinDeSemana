import random

def nextRandom():
    return round(random.random() * 100)

def addition(numbers):
    value = 0
    for num in numbers:
        value += num
        
    return value

def initValues():
    i=0
    numbers = []
    while i < 10:
        numbers.append(nextRandom())
        i = i+1

    return numbers

# MAIN
values = initValues()
sum = addition(values)
print("Values: ", values)
print("Sum: ", sum)

    
