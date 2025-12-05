# enter digit and get word insted
phone = input('Phone: ')


numbers = {
    '1': 'one',
    '2':'two',
    '3':'three',
    '4':'four',
}

output = ''

for ch in  phone:
    output += numbers.get(ch , '!') + ' '






print(output)