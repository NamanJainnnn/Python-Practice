#12345...n output req

if __name__ == '__main__':
    n = int(input())
    
one = 0

while one != n:
    one += 1
    print(one , end="")

print("* * " * 10)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
max_number = max(arr)
arr.remove(max_number)


