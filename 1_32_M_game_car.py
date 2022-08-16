print("""
How to play?
Let's see if you find out!
Have fun!""")

command = ""
while command.lower() != "help":
    command = input("> ").lower()
    if command.lower() != "help":
        print("pleas type 'help'")
    elif command == "help":
        print("""Pleas write:
    start - to sart car
    stop  - to stop car
    quit  - to exit""")

command_2 = ""
while True:
    command_2 = input("> ").lower()
    if command_2 == "start":
        print("car has started")
    elif command_2 == "stop":
        print("car has stopped")
    elif command_2 == "quit":
        break
    else:
        print("I don't understand!")
else:
    print("game over!")
