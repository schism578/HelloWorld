letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)    # prints alphabet backwards but doesn't include 'a' because it will return UP TO BUT NOT INCLUDING the end value of the slice

# How to print the 'a'?
backwardsWithA = letters[25::-1]    # setting the variable to equal letters[::-1] would work too
print(backwardsWithA)

# Slicing Challenges
sliceQPO = letters[16:13:-1]
print(sliceQPO)

sliceEDCBA = letters[4::-1]
print(sliceEDCBA)

sliceEight = letters[25:17:-1]
print(sliceEight)