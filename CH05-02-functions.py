# Read an input as integer
def inputAsInt():
    return int(input("Introduce a number: "))

# Check if a number is positive (bigger than zero)
def isPositive(num):
    if(num >= 0):
        return True
    else:
        return False

#Main
num = inputAsInt()
print(num, "is possitive: ", isPositive(num))
