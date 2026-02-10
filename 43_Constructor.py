class Point:
    

    def __init__(self,x,y):               #init==initialize
        self.x = x                        #self=reference    
        self.y = y                         # this method is called constructor
    
    
    def move(self):     
        print('move')

    def draw(self):
        print('draw')       

point1= Point(10,20)       
print(point1.x)   

point1.x = 11                #we can also update the values here!
print(point1.x)    


#so obv here point cannot exist without its coordinates and if we ask point1.y it will show a attribute error here
#to fic this we use constructor!
#it automatically calls itsdelf as soon as object is created
#now we dont need to write point1.x=10
#the constructor will call itself and show the point!