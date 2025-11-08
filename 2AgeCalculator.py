#Age Calculator

dob = input('Enter the year you were born in!')
cyear = input('Enter current year!')
print( int(cyear) - int(dob))
#here int is used to convert string into number coz without int py will take birth year as text like '2005' not 2005
print('*' * 50)

#Pounds in Kilo

weight = input('Enter your weight in pounds')
print( int(weight) / 2.204 + 'Kg')
