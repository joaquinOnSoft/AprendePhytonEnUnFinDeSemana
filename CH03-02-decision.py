import random

num1 = round(random.random() * 100)
num2 = round(random.random() * 100)

str = "is equal"

if(num1 > num2):
    str = "is bigger than"
elif (num1 < num2):
    str = "is smaller than"
else:
    str = "is equal"

print(num1, str, num2)
