
#here, name is like a variable inside a function
# just like we used to do all name=jhon snoe
#insted now we use this

def greet_user(first_name , last_name):
    print(f'Suppp {first_name} {last_name}')
    print('Welcome Aboard!')

print('Start')
greet_user('Jhon','Snow')
#here we used to write teo print lines again but this made  it simpler
greet_user('Jamie','Lanaster')
print('Finish')


#parameter is the 'name'
#and argument is the value of name i.e 'jhon snow'
#always supply value to parameters orelse u will get error!!!!!


#greet_user('Jhon',first_name='Snow') here position doesnot matter coz its a KEYWORD ARGUMENT!
#if not for key argument it would print snow jhon