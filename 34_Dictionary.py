# use {} to define dictionary

Character = {
    'Name':'Hope Mikaelson',
    'Age': 26,
    'is_G.O.A.T.' : True
}


print(Character['Name'])
print(Character['Age'])
print('IS GOAT: ' , Character['is_G.O.A.T.'])


print(Character.get('DPB'))
print(Character.get('Name'))
print(Character.get('DOB' , '31 October 1999'))

#we can upfate dictionary
Character['Name'] = 'Danielle'
print(Character['Name'])