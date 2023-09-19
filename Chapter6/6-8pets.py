animal1 = {
    'animal': 'dog',
    'owner': 'john',
}
animal2 = {
    'animal': 'hamster',
    'owner': 'jim',
}
animal3 = {
    'animal': 'cat',
    'owner': 'stacy',
}

allAnimals = [animal1, animal2, animal3]

for animal in allAnimals:
    for key, value in animal.items():
        print(f"{key.title()}: {value.title()}")