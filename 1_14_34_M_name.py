
name = input("Choose your name: ")
number = len(name)
if number < 3:
    print("Your name is too short.")
elif number > 10:
    print("Your name is too long.")
else:
    print("Your name looks good.")