max=0
numSet= [50, 4531, 352, 3453, 35355]
print('max=',max)
for count, i in enumerate(numSet):
    print('count is:',count)
    print('current is', i)
    print('max is now=',max)
    if i>max:
        max=i
        continue1=input('type y to continue?')
        print('')
        if continue1 == 'y':
            continue
print('Blastoff!')

