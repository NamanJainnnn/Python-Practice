names = ['Naman' , 'Danielle' , 'Powerful' , 'Humans' , 'Legend' ]
print(names)
print(names[0]) #index 0 is Naman hence output will be Naman & also -1 will give legend
print(names[0:2])
names[2] = "All mighty!" #changing or updating  the list (og)
print(names[:])


#mosh challenge:::Write a programm to find the largest number in the list!


numbers  = [10,50,69,67,11]
print(numbers)
 #i am thinking maybe we subtract each number with eachother in list and find max but the problem remain 
 #how tf we gonna find max! if we can find max then wht tf we are subtracting then
 #idk the maan i am going to eatch the mosh solution


 #Wow he beautifully used FOR loop to compair first number with each number which is adjucent
 #one by one and kept of changing the number!
 #very wise!

numbers  = [10,50,69,67,11]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(f'Max value: {max}')

#Use loops!!!!!!!Dont forget they exist!
       