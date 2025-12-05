#numbers = [2,2,4,6,3,4,6,1,2]
numbers = list(map(int, input("Enter Numbers Seperated By Space!").split()))
#pointer is the index
pointer = 0

#n is the value of rhe index
n = numbers[pointer]
print(n)

#no. of reps=== countnum
countnum = numbers.count(n)
print(countnum) 

while pointer < len(numbers):
   
    n = numbers[pointer]
    countnum = numbers.count(n)
   
    while countnum != 1:
        numbers.remove(n)
        countnum = numbers.count(n)
    pointer += 1


print(numbers)

#again this method is very unproductive, very long
# mosh did somethinf very simple