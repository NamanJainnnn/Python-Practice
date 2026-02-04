numbers = [9,6,6969,96,69]


max_value = numbers[0]
min_value = numbers[0]

for i in numbers[0:2]:
    if i > max_value:
        max_value = i

    if i < min_value:
        min_value = i
    
    
print(f' Maximum Value: {max_value}')
print(f' Minimum Value: {min_value}')

#___________________________________________________________________________________________________
e=""          #just to understand not nessary to write this line!
try:
    numbers = list(map(int , input("Enter Numbers here:(with spaces)").split()))
    if len(numbers) == 0:
         raise ValueError('Write at least one integer')

except ValueError as e:
    if str(e) == 'Write at least one integer':
      print('Write at least one integer')
    else:
        print('Invalid input. Please enter integers separated by spaces.')
    exit()

#we used 'as e' because except catchs all the error and including raise error msg 
#so except catchs the raise error msg and in the except block compaire the raise error with the error pyhton stored in the 'e'
#so we used 'as e' to catch the error and print it in except and get raise error msg differently



max_value = numbers[0]
min_value = numbers[0]

for i in numbers:
    if i > max_value:
        max_value = i

    if i < min_value:
        min_value = i 

print(f' Maximum Value: {max_value}')
print(f' Minimum Value: {min_value}')











