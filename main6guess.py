import random
ranNum = random.randint(0,1000)

while True:
    guessInt = int(input('Guess a number 0 to 1000:'))
    if guessInt<ranNum:
        print('too low!')

    elif guessInt>ranNum:
        print('too high!')

    else:
        print('bingo, the answer is:', guessInt)
