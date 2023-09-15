majorRivers = {
    'nile': 'egypt',
    'mississippi river': 'mississippi',
    'amazon': 'south america',
}

for river, place in majorRivers.items():
    print(f"The {river.title()} runs through {place.title()}.")

print("")
for river in majorRivers.keys():
    print(river.title())


print("")
for place in majorRivers.values():
    print(place.title())