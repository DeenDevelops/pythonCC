prompt = "How old are you? "


active = True

while active:
    age = input(prompt)
    age = int(age)

    if(age < 3):
        print("\nYour ticket is free.")
    elif(age >= 3 and age < 12 ):
        print("\nYour ticket is $10.")
    elif(age >= 12):
        print("\nYour ticket is $15.") #161