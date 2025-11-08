print('*' * 10 + 'Welcome to the guess game' + '*' * 10)


import random

number = random.randint(0,5)
guess = int(input('Enter guess between 0 and 5'))
guess_count = 0
guess_limit = 2


while guess>5:
    print('DUDE ANSWER WITHIN RANGE')
    guess = int(input('Enter guess between 0 and 5'))


while guess != number and guess_limit>0:
        
        print( f'TRY AGAIN! u have {guess_limit} guesses left')
        guess_limit -= 1
        guess = int(input('Enter guess between 0 and 5'))

        if guess_limit == 0:
              print('Game Over!Out of moves')
        if number == guess:
              print('Yay! U Won!!!')
        
        


print('GG!')


  