"""
This program gets the maximum number in a list named numSet
and stores the maximum number in a variable called:
maxNum
and then prints this.
"""

maxNum = 0
numSet = [56, 4531, 352, 3453, 35355]
for i in numSet :
    if i > maxNum:
        maxNum = i
print(maxNum)
