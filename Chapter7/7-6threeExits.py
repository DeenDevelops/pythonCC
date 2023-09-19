prompt = "\nHow old are you? "
prompt +="\n(Enter '-1' when you are finished)"


active = True

while active:
    age = input(prompt)
    age = int(age)

    if(age == -1 ):
        active = False
        break
    elif(age < 3):
        print("\nYour ticket is free.")
    elif(age >= 3 and age < 12 ):
        print("\nYour ticket is $10.")
    elif(age >= 12):
        print("\nYour ticket is $15.")