#                   1
#         012345678901234
parrot = "Norwegian Blue"

print(parrot)

# accessing string elements
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-1])   # start indexing at end of string, '-0' doesn't make numerical sense so start at '-1'
print(parrot[-14])  # since indexes start at '-1' in reverse, '-14' becomes 'N'

print()
# negative indexing for 'we win' like above
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

# where 14 is string.length
print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

print()

print(parrot[0:6])  # Norweg, 'slice' operator, UP TO BUT NOT INCLUDING the final indexed element
print(parrot[3:5])  # we
print(parrot[0:9])  # Norwegian
# OR...
print(parrot[:9])   # ALSO Norwegian, include everything from the first index element UP TO BUT NOT INCLUDING the 9th indexed element

print()

print(parrot[10:14])    # Blue
print(parrot[10:])      # ALSO Blue, slices everything from the start value to the end of the string length
print(parrot[:6] + parrot[6:])    # Norwegian Blue
print(parrot[:])                  # ALSO Norwegian Blue, not very valuable with strings

print()

print(parrot[-4:-2])    # Bl
print(parrot[-4:12])    # ALSO Bl

# can play around with this with indexes, negative indexes, and slicing
letters = "abcdefghijklmnopqrstuvwxyz"

# STEP within a slice
print(parrot[0:6:2])    # 2 designates how many elements to 'STEP' over for each increment through the slice
print(parrot[0:6:3])    # Here... 3 elements are stepped

number = "9,223,372,036,854,775,807"
print(number[1::4])     # show how to step through entire string

secondNumber = "9,223;372:036 854,775;807"
print(secondNumber[1::4])   # allows us to split out specific elements

# OR......
thirdNumber = "9,223;372:036 854,775;807"
separators = thirdNumber[1::4]
print(separators)

# OR......print the numbers in an array
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
