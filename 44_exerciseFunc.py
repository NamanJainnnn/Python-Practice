#create a object with function talk and name constructor

class Person:

    def __init__(self,name):
        self.name = name
    

    def talk(self):
        print(f"i am my fathers's daughter & i am gonna kill you {self.name}")




danielle = Person('monster')
danielle.talk()
print(danielle.name)

klaus = Person('vampire')
klaus.talk()