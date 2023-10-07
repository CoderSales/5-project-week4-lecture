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

# References:
# 
# primary reference:
# How to use case with inequalities | Stackoverflow :
# https://stackoverflow.com/questions/69710333/is-there-a-way-to-match-inequalities-in-python-%E2%89%A5-3-10
#
# secondary reference:
# general case for match case | geeksforgeeks :
# https://www.geeksforgeeks.org/python-match-case-statement/


scorePre=input("score from 0 to 100 : ")
score= int(scorePre)
match score:
    case _ if score>=80:
        print('A1')
    case _ if score>=72:
        print('A2')
    case _ if score>=64:
        print('B1')
    case _ if score>=60:
        print('B2')
    case _ if score>=56:
        print('B3')
    case _ if score>=52:
        print('C1')
    case _ if score>=48:
        print('C2')
    case _ if score>=40:
        print('C3')
    case _ if score>=35:
        print('D1')
    case _ if score>=30:
        print('D2')
    case _ if score<30:
        print('F, fail')
