str = "En Un Lugar De La Mancha"

print("\n upper & lower ------ \n")
print(str.upper())
print(str.lower())
print("Length: ", len(str))

str2 = "abcdefg "
str3 = "1234567890"

print("\n isalnum ------")
print(str, " --> ", str2.isalnum())
print(str2, " --> ", str2.isalnum())
print(str3, " --> ", str3.isalnum())

print("\n isdigit ------")
print(str, " --> ", str2.isdigit())
print(str2, " --> ", str2.isdigit())
print(str3, " --> ", str3.isdigit())

print("\n isupper ------")
print(str, " --> ", str.isupper())
print(str2, " --> ", str2.isupper())
print(str3, " --> ", str3.isupper())

print("\n islower ------")
print(str, " --> ", str.islower())
print(str2, " --> ", str2.islower())
print(str3, " --> ", str3.islower())

print("\n swapcase ------")
print(str, " --> ", str.swapcase())
print(str2, " --> ", str2.swapcase())
print(str3, " --> ", str3.swapcase())

str4 = "   He tenido una pesadilla. He visto un 2 "
print("\n strip ------")
print(str4.lstrip())
print(str4.rstrip())
print(str4.strip())

print("\n replace ------")
print(str.replace('Mancha', 'Luna'))
