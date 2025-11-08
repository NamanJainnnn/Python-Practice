import random

answer = random.randint(1,10)
guess = int(input('Guess Number between 1 and 10'))

while guess != answer:
    print('NOPE!!!!!Try Again ;)')
    guess = int(input('Enter Again'))

print('GG!')
#mosh also added limited number of guesses by adding +1 nad setting while to <3 
#he used if and else statements too
#he used BREAK to end a loop!
#he game is great obly drawback once played u will know the answer

#REMAKE THIS GAME !!!MOSH+RANDOM=NAMANS GAME