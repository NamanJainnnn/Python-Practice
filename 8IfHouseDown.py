# price of house is 1million dollors 
# if buyer has good credit! they need to put down 10%
#if not then 20%

is_good= False
is_bad= True

if is_good:
    print('Your credit score is good you need to put 10% downpayment')
    x= 1000000 * 0.1
    print("that is " + str(x) + 'USD')

elif is_bad:
    print('Your credit score is bad you need to put 20% downpayment')
    x= 1000000 * 0.2
    print("that is " + str(x) + 'USD')
else:
    print("Sorry dude u dont have enought money!")

print('Congrats for your new house!')
# mosh use f string and a bit more variables but mine is absoutly correct!

    







