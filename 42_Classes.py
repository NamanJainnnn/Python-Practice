#we learmed what list is string is and all that but what if we want a cart, then we define new type with class


class Point:
    def move(self):     #defining the funvtion move in ehivh if called it will print "move"
        print('move')

    def draw(self):
        print('draw')        #these are methods of class... methods=function i guess


point1= Point()                #we are storing the the class in variable    #this is object with the class point()
point1.draw()             #here python recommends functions of a class coz above we defined it eg(draw,move)
point1.x = 69                 #we can give attributes to the class
print(point1.x)
