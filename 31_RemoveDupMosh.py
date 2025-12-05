numbers = [2,2,4,6,3,4,6,1]
# numbers = list(map(int, input().split()))

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)

#first we take an empty array
#then use for loop to iterate
#use if,is,not to fill numbers
#ChatGPT tolf me goest think how, think what
#coz i am writing the whole logic insted of using builtin functions
