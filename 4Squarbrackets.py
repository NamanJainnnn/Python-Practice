statement = 'I love Night'
print(statement[0:10])
#squar brackets are used to print only particular letters or line of the whole output use : for line and simpl num for one letter

course = 'python for beginners'
another = course[:]
print (another)
#py will asume empty brackets as 0 and end of string...used to copy!
#if u wanna print jhon [snow] u can not do it directly
#use formate string i.e f string
# new variable = f'({name} [{lastname}]'

name= 'Jhon'
last='snow'
msg= f'{name} [{last}] is a coder'
print(msg)