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

# declare variables
retry=None
score_pre=None
decision=None

def initialise(param_score):
    retry=False
    score_pre=param_score
    return retry, score_pre

score_pre = initialise(score_pre)[1] # updates score_pre
retry = initialise(score_pre)[0] # updates retry

def input_function():
    score=input("score from 0 to 100 : ")
    return score

score = input_function() # has user guess

def integer(score_pre):
    """
    The integer function:
    - Takes user input
    - and turns it into an integer stored in store.
    - then returns the score variable which contains that integer.    
    """
    score = int(score_pre)
    return score


def check():
    """
    checks if the score is in the range from:
    - 0 to
    - 100.
    """
    if score >=0 & score <= 100:
        retry=False
    else:
        retry=True


retry,scorePre = initialise() # retry False, scorePre
scorePre = input(scorePre) # '80'
score = integer() # #80
retry = check() # True
decide(retry, score)

def decide(retry, score):
    """
    # decision=Null
    In this function I am trying to use a variable called decision,
    which seems to need to be set to something like Null
    to be usable. (Hence the above commented code line moved intot eh Docstring.)
    
    Below there is an if statement that tests to see if retry is True
    - if retry is True (meaning neceesray to retry)
    - call the input function.
    - else:
    - call the check function and pass in a variable called score.
    
    Unfinished.
    """
    if retry==True:
        input()
    else:
        check(score)

def check(score):
    """
    The check function takes 1 argument called score.
    
    It then checks what range the score is in,
    in order to assign a letter grade.
    """
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
    elif score<30:
        print('F, fail')

