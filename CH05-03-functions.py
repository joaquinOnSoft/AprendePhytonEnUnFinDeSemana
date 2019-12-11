# Read an input as integer
def inputAsInt():
    return int(input("Introduce a number: "))

# Addition of two number
def addition(num1, num2):
    return num1 + num2

# Substraction of two number
def substraction(num1, num2):
    return num1 - num2

# Multiplication of two number
def multiplication(num1, num2):
    return num1 * num2

# Division of two number
def division(num1, num2):
    return num1 / num2


#Main
num1 = inputAsInt()
num2 = inputAsInt()
print(num1, " + ", num2, " = ", addition(num1, num2))
print(num1, " - ", num2, " = ", substraction(num1, num2))
print(num1, " * ", num2, " = ", multiplication(num1, num2))
print(num1, " / ", num2, " = ", division(num1, num2))
