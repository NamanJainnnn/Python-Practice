#mosh challenge:::Write a programm to find the largest number in the list!
numbers  = [10,50,69,67,11]
max_value = numbers[0]
for i in numbers:
    if i > max_value:
        max_value = i
print(max_value)



if __name__ == '__main__':
    n = int(input())
    
for i in range(n):
    print(i**2)


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 == 0 and year%100 == 0 and year%400 ==0:
        leap = True
    return leap

year = int(input())
print(is_leap(year))