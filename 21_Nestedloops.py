for x in range(4):
    for y in range(3):
        print(x,y)


#Mosh challenge to print F using X's
num = [5,2,5,2,2]
Star = "x"

for num in num:
    print(num * "x")
#this is cheating he says u must use nested loops 

num = [5,2,5,2,2]

for x_count in num:
    output = ""
    for item in range(x_count):
        output += 'X'
    print(output)
#this is correcct coz we are using nested loop
#taking the range as xcount and then adding it to output'x'


print("                                   ")

char = [5,1,1,1,5]
for lenght in char:
    output=""
    for item in range(lenght):
        output += "x"
    print(output)

print("                                   ")

char = [1,1,1,1,5]
for length in char:
    output=""
    for row in range(length):
        if length==1:
            output += "x"  
            print(output , end = "    X")
        else:
            output += "x"
            print(output)
    
print(output)
#nested loops are shit!
           