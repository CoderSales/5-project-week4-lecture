# Exercise 3: 
    
# Write a program to prompt for a score between 0 and 100.
# If the score is out of range, print an error message. 
# If the score is between 0 and 100, 
# print a grade using the following table: 
# 30% D2
# 35% D1
# 40% C3
# 48% C2
# 52% C1
# 56% B3
# 60% B2
# 64% B1
# 72% A2
# 80% A1

scorePre=input("score from 0 to 100 : ")
score= int(scorePre)
if score>=80:
    print('A1')
elif score>=72:
    print('A2')
elif score>=64:
    print('B1')
elif score>=60:
    print('B2')
elif score>=56:
    print('B3')
elif score>=52:
    print('C1')
elif score>=48:
    print('C2')
elif score>=40:
    print('C3')
elif score>=35:
    print('D1')
elif score>=30:
    print('D2')

