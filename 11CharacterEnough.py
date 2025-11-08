#PROBLEM:::If name is less then three character long!=name must be atleasst 3 character long
#if more than 50 character ==max of 50 characters
#otherwise name looks good!
print("_" * 50)


name = input("Enter Your Beautiful Name!")
length = len(name)

if length < 3:
    print('Name must be atleast 3 characters long')

elif length > 50:
    print('Name can be a maximum of 50 characters long!')

else:
    print('Name looks good')