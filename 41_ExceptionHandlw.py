age = int(input('Enter age: '))
print(age)

#now if the user inputs something which isnot a number
#then the whole program wil crash
# Eg::instead of 20 if we type iloveD the program will crash and show VALUEERROR
#so to handel that we use TRY::EXCEPT

try:
    age = int(input('Enter age: '))
    print(age)

except ValueError:
    print('Invalid Input')

#Now our programm doest crash but gives a proper message

#if we put age ZERO then there wil be ZeroDivisionError so handel that as well we add another exception
try:
    age = int(input('Enter age: '))
    income = 20000
    risk = income / age
    print(age)

except ZeroDivisionError:
    print('Age cannot be zero dumass')

except ValueError:
    print('Invalid Input')