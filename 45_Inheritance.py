class Mammle:
    def walk(self):
        print('I AM WALKING')


class Dog(Mammle):
    pass   #to do nothing or u can give a function too.....


class Cat(Mammle):
    def hit(self):
        print('Target now bleeding!')

#we had to write all the WALK code for dog and cat too 
#now we create a mammle class to to inherite the properties of mammle class

husky = Dog()
husky.walk()

furry = Cat()
furry.hit()