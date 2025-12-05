numbers = [2,2,4,6,3,4,6,1]

#for 2
count2 = int(numbers.count(2))
while count2 != 1:
    numbers.remove(2)
    break

#for 3

count4 = int(numbers.count(4))
while count4 != 1:
    numbers.remove(4)
    break
#for 6
count6 = int(numbers.count(6))
while count6 != 1:
    numbers.remove(6)
    break

print(numbers)
numbers.sort()
print(numbers)

#this is long and waste of time i think
#what if we take input as list!
#then we use index
#AND THEN remove it and move forword