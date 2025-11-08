print('*' * 10 + 'Welcome to the guess game' + '*' * 10)


import random

number = random.randint(0,5)
guess = int(input('Enter guess between 0 and 5'))

while guess>5:
    print('DUDE ANSWER WITHIN RANGE')
    guess = int(input('Enter guess between 0 and 5'))


while guess != number:
        print('TRY AGAIN!')
        guess = int(input('Enter guess between 0 and 5'))


print('GG!')



  