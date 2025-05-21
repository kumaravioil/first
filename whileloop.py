while True:
    print("Who are you?")
    name=input()
    if name!= "Kumar":
        continue
    print("Hello, Kumar. What is the password?")
    password=input()
    if password=="secret":
        break
    print("Incorrect password")