numbers = [69,96,3,6,5,6,9]

#to add new item:::append

numbers.append(69)
print(numbers)

#to add at certain point

numbers.insert(5,6969)
print (numbers)

# to remove

numbers.remove(6969)
print(numbers)

#numbers.clear()
#print(numbers)


#to remove last item in a list
numbers.pop()
print(numbers)

#returns the index of the item in a list

print(numbers.index(6))

#using in to find number

print( 50 in numbers)

#to count reps of numbers

print(numbers.count(6))

numbers.sort()    #assending order
print(numbers)

numbers.sort()  #for decending order
numbers.reverse()  #to reverse the list
print(numbers)


number2 = numbers.copy() #to copy list!! changes made in og list will not show here!
#like lets add 6.9 here
numbers.append(10)

print(number2)