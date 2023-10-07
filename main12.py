maxNum = 0
numSet = [56, 700, 4531, 352, 3453, 35355]
for count, i in enumerate(numSet) :
    # print('line 4: type(i) is: ',type(i))
    # print('line 5 type(maxNum) is: ', type(maxNum))
    print('line 6 i is: ',i)
    # print("count is: ", count)
    print("pre, maxNum= ",maxNum)
    maxNum = maxNum + i
    print("post maxNum=maxNum+i, maxNum =", maxNum)
    if count==(len(numSet)-1):
        print("count==(len(numSet)-1)== ", (len(numSet)-1))
print("maxNum+i=",maxNum)
