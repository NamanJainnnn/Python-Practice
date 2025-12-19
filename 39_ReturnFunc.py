def square (number):
    return number*number

print(square(3))

#by default every function gives NONE to change that
#espically in claculation to avoid NONE we use return

#use RETURN when u need to store and reuse the value like
#total  = add(a,d)
#discount = total - 10%
#Use RETURN here Not PRINT coz we are reuseng the vvalue again!!



def rect (number):
    print( number*number)

print(rect(2))
#this is whats happnes if we use PRINT instead of Return