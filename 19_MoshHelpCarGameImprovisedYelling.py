print("Welcome to Dr. Driving Mate!")
command = ""
started = False

while True:
    command = input('> ').lower()

    if command == "start":
        if started:
            print('Dude car is already started')
        else:
            started = True
            print('Car Started!')

    elif command == "stop":
        if not started:
            print('Dude car is already stopped')
        else:
            started = False
            print('Car Stopped!')

    elif command == "help":
        print("""
Start - To start the car
Stop - To stop the car
Quit - To quit the game
""")
        
    elif command == "quit":
        print("Quitting the game")
        break

    else:
        print('Dude wtf enter a valid command!')