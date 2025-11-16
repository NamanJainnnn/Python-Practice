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



