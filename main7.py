import random
ranNum = random.randint(0,1000)

while True:
    guess = int(input('input a number: '))
    if guess==ranNum:
        print('Done!')
        break
    elif guess<ranNum:
        print('too low!')
    
    elif guess>ranNum:
        print('too high!')
