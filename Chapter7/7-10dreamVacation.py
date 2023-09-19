vacations = {}

active = True

while active:
    name = input('Enter your name: ')
    place = input('Where would you go on a dream vacation? ')
    repeat = input('Would you like to add another person? (y/n)')

    vacations[name] = place

    if repeat == 'n':
        active = False

print("")
for name, place in vacations.items():
    print(f"{name.title()} would like to go to {place.title()}.")