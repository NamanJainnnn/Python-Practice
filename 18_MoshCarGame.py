print('Welcome to DR.Driving how may i assist u')
starting = input(">")

while starting.lower() != "help":
    print("Can't assist u rn!")
    starting = input(">")

    if starting.lower() == "help":
     print('''
          Start - to start the car
          stop - to stop the car
          quit - to quit the game
          ''') 
     
command = input(">")

while command.lower() != "quit":
    
    if command.lower() == "start":
        print('Car Started...Ready To Go!')
        command = input(">")
    

    if command.lower() == "stop":
       print("Car Stopped")
       command = input(">")

    if command.lower() == "quit":
       print("Quitting the game")

       break
    
    else:
       print("Sorry! Please choose from the options!")
       command = input("Enter Valid Command PLease Mate")

print('Thanks for Playing :)')

 
    


