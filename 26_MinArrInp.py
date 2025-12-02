if __name__ == '__main__':
    n = int(input("enter number"))
    arr = list(map(int, input().split()))
    
highest = max(arr)
while highest in arr:
    arr.remove(highest)
    
print(max(arr))


#List----converts something to list
#map------give property to everyone
#split------to split big string into small parts
#int ---------to convert str into int
